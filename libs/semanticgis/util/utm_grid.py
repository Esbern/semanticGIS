import geopandas
from shapely.geometry import Polygon, box, MultiPolygon
import math
import pandas as pd
from typing import List, Callable, Union, Tuple, Optional

# --- Helper function for Danish-specific filename generation (can be default) ---
def _generate_danish_utm_filename(
    dataset_prefix: str,
    x_part: int,
    y_part: int,
    data_format: str,
    crs_name_for_filename: str
) -> str:
    """
    Generates a filename following the Danish convention (e.g., DTM_623_44_TIF_UTM32-ETRS89).
    x_part and y_part are assumed to be the integer coordinate parts derived from
    (coordinate // cell_size_meters).
    """
    return f"{dataset_prefix}_{x_part}_{y_part}_{data_format}_{crs_name_for_filename}"

# --- Main Generic Function for the datafetch library ---
def get_intersecting_utm_grid_cells(
    aoi_path: str,
    target_crs_epsg: int,
    cell_size_meters: int,
    dataset_prefix: str,
    data_format: str,
    crs_name_for_filename: Optional[str] = None, # Make optional, can often be derived
    filename_pattern_func: Callable[[str, int, int, str, str], str] = _generate_danish_utm_filename
) -> List[str]:
    """
    Returns a list of UTM grid filenames that intersect the given AOI polygon.
    This function is generic for any UTM grid system, with a default
    Danish naming convention.

    Args:
        aoi_path (str): Path to the GeoParquet file containing the AOI polygon(s).
        target_crs_epsg (int): The EPSG code for the desired UTM coordinate system
                               (e.g., 25832 for ETRS89 UTM Zone 32N, 25833 for UTM Zone 33N).
        cell_size_meters (int): The size of the grid cells in meters (e.g., 1000 for 1km, 10000 for 10km).
        dataset_prefix (str): The prefix for the dataset (e.g., "DTM", "ORTHO").
        data_format (str): The data format string (e.g., "TIF", "LAZ").
        crs_name_for_filename (str, optional): The CRS name string to be included in the filename
                                                (e.g., "UTM32-ETRS89"). If None, attempts to derive
                                                a generic UTM name.
        filename_pattern_func (Callable): A function to generate the filename string.
                                          Defaults to `_generate_danish_utm_filename`.
                                          Signature: (dataset_prefix, x_part, y_part, data_format, crs_name_for_filename) -> str.

    Returns:
        List[str]: A list of filenames of intersecting grid cells.
    """
    try:
        # Load AOI
        aoi_gdf = geopandas.read_parquet(aoi_path)
        
        if aoi_gdf.crs is None:
            # Critical error: Cannot reproject if input CRS is unknown.
            raise ValueError(f"AOI from {aoi_path} has no CRS defined. Please ensure the GeoParquet includes CRS information.")
            
        # Reproject to target CRS if necessary
        if aoi_gdf.crs.to_epsg() != target_crs_epsg:
             print(f"Reprojecting AOI from {aoi_gdf.crs.to_string()} to EPSG:{target_crs_epsg}...")
             aoi_gdf = aoi_gdf.to_crs(epsg=target_crs_epsg)
        else:
            print(f"AOI is already in target CRS EPSG:{target_crs_epsg}.")

        # Handle multiple geometries in AOI by dissolving them into a single (possibly multi-part) polygon
        # This simplifies intersection logic, but assumes you want files that intersect *any* part of the AOI.
        aoi_geometry = aoi_gdf.geometry.unary_union
        
        if aoi_geometry.is_empty:
            print("Warning: AOI geometry is empty after loading/reprojection. No intersecting cells will be found.")
            return []
            
        # If the AOI is a Point or Line, convert to its bounding box for intersection with grid cells
        if aoi_geometry.geom_type in ['Point', 'LineString', 'MultiPoint', 'MultiLineString']:
            print(f"Warning: AOI type is {aoi_geometry.geom_type}. Using its bounding box for intersection.")
            aoi_polygon = box(*aoi_geometry.bounds)
        elif aoi_geometry.geom_type in ['Polygon', 'MultiPolygon']:
            aoi_polygon = aoi_geometry
        else:
            raise TypeError(f"Unsupported AOI geometry type: {aoi_geometry.geom_type}")


    except Exception as e:
        print(f"Error in AOI processing from {aoi_path}: {e}")
        return []

    min_x, min_y, max_x, max_y = aoi_polygon.bounds

    # Determine Grid Index Range directly from coordinates
    # We use floor for the start (min) and ceil for the end (max) of the coordinate parts.
    # This ensures we cover all cells that spatially overlap the AOI's bounding box.
    start_x_coord_part = math.floor(min_x / cell_size_meters)
    end_x_coord_part = math.ceil(max_x / cell_size_meters)

    start_y_coord_part = math.floor(min_y / cell_size_meters)
    end_y_coord_part = math.ceil(max_y / cell_size_meters)

    intersecting_filenames: List[str] = []

    # If crs_name_for_filename is not provided, try to derive a generic one
    if crs_name_for_filename is None:
        try:
            # This is a very basic attempt. For production, you might have a lookup table
            # or a more sophisticated way to get the string representation.
            # Example: ETRS89 / UTM zone 32N has EPSG:25832
            # proj_name = aoi_gdf.crs.name # Not always ideal for filename
            # For UTM, it often follows a pattern like "UTM{zone}-{datum}"
            
            # Use pyproj to get a more robust name if needed, or define a mapping
            # For simplicity for this example, we'll just use a generic format if not provided.
            if target_crs_epsg in [25832, 25833]: # Common Danish CRSs
                 crs_name_for_filename = f"UTM{target_crs_epsg - 25800}-ETRS89"
            else:
                 crs_name_for_filename = f"EPSG{target_crs_epsg}" # Fallback
        except Exception:
            crs_name_for_filename = f"EPSG{target_crs_epsg}" # Fallback if derivation fails


    for current_x_coord_part in range(int(start_x_coord_part), int(end_x_coord_part)):
        for current_y_coord_part in range(int(start_y_coord_part), int(end_y_coord_part)):
            # Construct Cell Bounding Box in meters based on the integer coordinate parts
            cell_min_x = current_x_coord_part * cell_size_meters
            cell_min_y = current_y_coord_part * cell_size_meters
            cell_max_x = cell_min_x + cell_size_meters
            cell_max_y = cell_min_y + cell_size_meters

            cell_polygon = box(cell_min_x, cell_min_y, cell_max_x, cell_max_y)

            # Check for Intersection
            if aoi_polygon.intersects(cell_polygon):
                # Generate Filename using the provided or default pattern function
                filename = filename_pattern_func(
                    dataset_prefix,
                    current_x_coord_part,
                    current_y_coord_part,
                    data_format,
                    crs_name_for_filename
                )
                intersecting_filenames.append(filename)

    return intersecting_filenames

# --- Example Usage for your datafetch library ---
if __name__ == "__main__":
    # Create dummy AOI GeoParquet files for testing
    # AOI 1: In EPSG:25832 (Danish UTM32)
    aoi_polygon_dk_utm32 = Polygon([
        (550000, 6100000), (560000, 6100000), (560000, 6110000), (550000, 6110000), (550000, 6100000)
    ])
    gdf_dk_utm32 = geopandas.GeoDataFrame(
        pd.DataFrame({'id': [1], 'name': ['DK UTM32 AOI']}), 
        geometry=[aoi_polygon_dk_utm32], 
        crs="EPSG:25832"
    )
    test_aoi_dk_utm32_path = "test_aoi_dk_utm32.parquet"
    gdf_dk_utm32.to_parquet(test_aoi_dk_utm32_path)
    print(f"Dummy AOI (in EPSG:25832) saved to {test_aoi_dk_utm32_path}")

    # AOI 2: In WGS84 (to test reprojection)
    aoi_polygon_wgs84 = Polygon([
        (10.3, 55.4), (10.4, 55.4), (10.4, 55.5), (10.3, 55.5), (10.3, 55.4)
    ])
    gdf_wgs84 = geopandas.GeoDataFrame(
        pd.DataFrame({'id': [2], 'name': ['WGS84 AOI']}), 
        geometry=[aoi_polygon_wgs84], 
        crs="EPSG:4326" # WGS84
    )
    test_aoi_wgs84_path = "test_aoi_wgs84.parquet"
    gdf_wgs84.to_parquet(test_aoi_wgs84_path)
    print(f"Dummy AOI (in EPSG:4326) saved to {test_aoi_wgs84_path}")

    # --- Test Case 1: Danish DTM, 10km grid, AOI already in UTM32 ---
    print("\n--- Test Case 1: Danish DTM, 10km grid, AOI in UTM32 ---")
    intersecting_files_10km_utm32 = get_intersecting_utm_grid_cells(
        aoi_path=test_aoi_dk_utm32_path,
        target_crs_epsg=25832,
        cell_size_meters=10000, # 10 km
        dataset_prefix="DTM",
        data_format="TIF",
        crs_name_for_filename="UTM32-ETRS89"
    )
    print(f"Found {len(intersecting_files_10km_utm32)} intersecting 10km grid files:")
    for filename in intersecting_files_10km_utm32:
        print(filename)

    # --- Test Case 2: Danish Orthophotos, 1km grid, AOI in WGS84 (will be reprojected) ---
    print("\n--- Test Case 2: Danish Orthophotos, 1km grid, AOI in WGS84 (reprojected to UTM32) ---")
    intersecting_files_1km_reprojected = get_intersecting_utm_grid_cells(
        aoi_path=test_aoi_wgs84_path,
        target_crs_epsg=25832, # Still target UTM32
        cell_size_meters=1000, # 1 km
        dataset_prefix="ORTHO",
        data_format="JP2",
        crs_name_for_filename="UTM32-ETRS89"
    )
    print(f"Found {len(intersecting_files_1km_reprojected)} intersecting 1km grid files:")
    for i, filename in enumerate(intersecting_files_1km_reprojected):
        if i < 10: print(filename) # Print first few
        elif i == 10: print("...")
    if len(intersecting_files_1km_reprojected) > 10:
        print(f"(and {len(intersecting_files_1km_reprojected) - 10} more)")
        
    # --- Test Case 3: Danish Lidar, 1km grid, different filename function (example for future flexibility) ---
    def _generate_alt_filename(dataset_prefix, x_part, y_part, data_format, crs_name_for_filename):
        # Example of a different naming convention, e.g., Y_X_DATASET.FORMAT
        return f"{y_part}_{x_part}_{dataset_prefix}.{data_format}"
        
    print("\n--- Test Case 3: Danish Lidar, 1km grid, using alternate filename pattern ---")
    intersecting_files_alt_naming = get_intersecting_utm_grid_cells(
        aoi_path=test_aoi_dk_utm32_path, # Using the original DK UTM32 AOI
        target_crs_epsg=25832,
        cell_size_meters=1000,
        dataset_prefix="LIDAR",
        data_format="LAZ",
        crs_name_for_filename="UTM32-ETRS89", # This part might be ignored by alt func
        filename_pattern_func=_generate_alt_filename # Pass in the custom function
    )
    print(f"Found {len(intersecting_files_alt_naming)} intersecting 1km grid files (alt naming):")
    for filename in intersecting_files_alt_naming:
        print(filename)