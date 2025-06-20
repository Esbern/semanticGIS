import duckdb
import geopandas as gpd
from semanticgis.abstract.pipeline import Pipeline

def _topological_sort(nodes, edges) -> list:
    # This implementation is correct.
    # ... (code from previous response)
    sorted_nodes = []
    nodes_to_visit = set(nodes.keys())
    edges = list(edges) 
    while nodes_to_visit:
        nodes_without_incoming_edges = set(nodes_to_visit)
        for from_node, to_node in edges:
            if to_node in nodes_without_incoming_edges:
                nodes_without_incoming_edges.discard(to_node)
        if not nodes_without_incoming_edges:
            raise ValueError("Pipeline contains a cycle.")
        for node_id in sorted(list(nodes_without_incoming_edges)):
            sorted_nodes.append(node_id)
            nodes_to_visit.remove(node_id)
            edges = [edge for edge in edges if edge[0] != node_id]
    return sorted_nodes

def _get_geometry_column(conn, table_name: str) -> str:
    """
    Intelligently finds the single geometry column in a DuckDB table.

    Raises:
        ValueError: If zero or more than one geometry column is found.
    """
    schema = conn.execute(f"DESCRIBE {table_name};").fetchall()
    
    # Find all columns with the GEOMETRY type
    geometry_columns = [col_name for col_name, col_type, _, _, _, _ in schema if col_type == 'GEOMETRY']
    
    if len(geometry_columns) == 0:
        raise ValueError(f"No geometry column was found in table '{table_name}'.")
    
    if len(geometry_columns) > 1:
        raise ValueError(
            f"Multiple geometry columns found in table '{table_name}': {geometry_columns}. "
            "semanticGIS currently requires an unambiguous single geometry column for spatial operations."
        )
    
    # If we get here, there is exactly one geometry column
    return geometry_columns[0]

def compile(pipeline: Pipeline, fetch_results: list = None) -> dict:
    """Executes the abstract pipeline using a DuckDB-centric engine."""
    node_id_to_table_map = {} 
    name_to_table_map = {}
    
    conn = duckdb.connect()
    conn.execute("INSTALL spatial; LOAD spatial;")
    conn.execute("INSTALL httpfs; LOAD httpfs;")

    try:
        # We use a topological sort for correct execution order.
        execution_order = _topological_sort(pipeline.nodes, pipeline.edges)
        print(f"✅ Pipeline execution started. Order: {execution_order}")

        for node_id in execution_order:
            node_data = pipeline.nodes[node_id]
            op_name = node_data.get('operation', '')
            output_name = node_data.get('output_name')
            
            print(f"  -> Executing Step: '{node_data.get('label', node_id)}'...")

            def get_input_table(op_node_data):
                input_name = op_node_data.get('input_name')
                # A helper to find the node ID for a given declared name
                input_node_id = next((nid for nid, ndata in pipeline.nodes.items() if ndata.get('output_name') == input_name), None)
                if not input_node_id: raise ValueError(f"Input name '{input_name}' not found.")
                return node_id_to_table_map[input_node_id]

            if 'vector.load' in op_name:
                source_path = node_data.get('source')
                table_name = f"tbl_{node_id}"
                sql = f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM ST_Read(?);"
                conn.execute(sql, [source_path])
                node_id_to_table_map[node_id] = table_name
                if output_name: name_to_table_map[output_name] = table_name
                print(f"     ✅ Loaded data into table '{table_name}'.")

            elif 'vector.filter_by_sql' in op_name:
                input_table = get_input_table(node_data)
                where_clause = node_data.get('where_clause')
                table_name = f"tbl_{node_id}"
                conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM {input_table} WHERE {where_clause};")
                node_id_to_table_map[node_id] = table_name
                if output_name: name_to_table_map[output_name] = table_name
                print(f"     ✅ Filtered '{input_table}' into new table '{table_name}'.")

            elif 'vector.buffer' in op_name:
                input_table = get_input_table(node_data)
                distance = node_data.get('distance')
                table_name = f"tbl_{node_id}"
                geom_col_name = _get_geometry_column(conn, input_table)
                print(f"     INFO: Found geometry column '{geom_col_name}' for buffering.")
                
                # YOUR SUPERIOR LOGIC:
                sql = f"""
                    CREATE OR REPLACE TABLE {table_name} AS
                    SELECT * EXCLUDE ({geom_col_name}),
                           ST_Buffer({geom_col_name}, {distance}) AS {geom_col_name}
                    FROM {input_table};
                """
                conn.execute(sql)
                
                node_id_to_table_map[node_id] = table_name
                if output_name: name_to_table_map[output_name] = table_name
                print(f"     ✅ Buffered '{input_table}' into new table '{table_name}'.")
        
        print("✅ Pipeline execution finished successfully.")
        
        final_results = {}
        if fetch_results:
            for name in fetch_results:
                table_to_fetch = name_to_table_map.get(name)
                if table_to_fetch:
                    print(f"     Fetching final  v1 result '{name}' from table '{table_to_fetch}'...")
                    
                    geom_col_to_fetch = _get_geometry_column(conn, table_to_fetch)
                    sql_fetch = f"SELECT *, ST_AsWKB({geom_col_to_fetch}) as _wkb_geom_ FROM {table_to_fetch}"
                    result_df = conn.query(sql_fetch).to_df()
                    
                    # --- THE FINAL, EXPLICIT TYPE CONVERSION ---
                    # Convert the bytearray column to a series of bytes objects
                    wkb_bytes = result_df['_wkb_geom_'].apply(bytes)
                    
                    # Create the GeoSeries from the corrected bytes series
                    geometry_series = gpd.GeoSeries.from_wkb(wkb_bytes)
                    
                    # Create the final GeoDataFrame
                    gdf = gpd.GeoDataFrame(
                        result_df.drop(columns=[geom_col_to_fetch, '_wkb_geom_']),
                        geometry=geometry_series,
                        crs="EPSG:4326"
                    )
                    final_results[name] = gdf
        
        conn.close()
        return final_results
        
        conn.close()
        return final_results

    except Exception as e:
        print(f"     ❌ FAILED on step '{node_id}': {e}")
        conn.close()
        return {}