
import yaml
from typing import Dict, List, Tuple, Optional, Union,Any # For type hinting
import importlib_resources # For robust access to package data files

import geopandas as gpd
from shapely.geometry import box


_cached_predefined_grids: Optional[Dict[str, Dict]] = None

def _get_grid_definitions_filepath():
    """Gets the path to the predefined_grids.yaml file."""
    # Uses importlib_resources to safely access package data
    # Assumes predefined_grids.yaml is in a 'data' subdirectory of the current package
    try:
        return importlib_resources.files(__package__).joinpath("data", "predefined_grids.yaml")
    except AttributeError: # Fallback for older importlib_resources or structure
        try:
            return importlib_resources.files(f"{__package__}.data").joinpath("predefined_grids.yaml")
        except Exception as e:
            # Handle cases where the path resolution might differ or fail
            # This might need adjustment based on your exact package structure
            # For a flat structure (yaml in same dir as this .py file):
            # return importlib_resources.files(__package__).joinpath("predefined_grids.yaml")
            raise RuntimeError(f"Could not locate predefined_grids.yaml: {e}")


def load_predefined_grids(force_reload: bool = False) -> Dict[str, Dict]:
    """
    Loads predefined grid definitions from the YAML file.
    Caches the result for subsequent calls unless force_reload is True.
    """
    global _cached_predefined_grids
    if _cached_predefined_grids is None or force_reload:
        filepath = _get_grid_definitions_filepath()
        try:
            with filepath.open('r', encoding='utf-8') as f:
                _cached_predefined_grids = yaml.safe_load(f)
                if not isinstance(_cached_predefined_grids, dict):
                    # Handle case where YAML is valid but not a top-level dictionary
                    _cached_predefined_grids = {} # Or raise error
        except FileNotFoundError:
            print(f"Warning: Predefined grids file not found at {filepath}")
            _cached_predefined_grids = {}
        except yaml.YAMLError as e:
            print(f"Error parsing predefined grids YAML file: {e}")
            _cached_predefined_grids = {} # Or re-raise
    return _cached_predefined_grids if _cached_predefined_grids is not None else {}

def get_predefined_grid(name: str) -> Optional[Dict[str, Union[str, float, int]]]:
    """
    Retrieves a specific predefined grid definition by its name.
    Returns None if the grid name is not found.
    """
    grids = load_predefined_grids()
    return grids.get(name)

def list_predefined_grid_names() -> List[str]:
    """Returns a list of names of all available predefined grids."""
    grids = load_predefined_grids()
    return list(grids.keys())

def get_all_predefined_grids() -> Dict[str, Dict]:
    """Returns a dictionary of all predefined grid definitions."""
    return load_predefined_grids().copy() # Return a copy to prevent modification of cache



def get_intersecting_grid_cells(
    aoi_geometry: Any,  # Expecting a single shapely geometry object
    aoi_crs: str,
    grid_definition: Dict[str, Any]
) -> List[Tuple]:
    """
    Calculates the grid cells that intersect with a given Area of Interest (AOI).

    Args:
        aoi_geometry (Any): A shapely geometry object representing the AOI.
        aoi_crs (str): The CRS of the input AOI geometry (e.g., "EPSG:4326").
        grid_definition (Dict[str, Any]): A valid grid definition dictionary.

    Returns:
        List[Tuple]: A list of unique grid cell identifier tuples.
    """
    # Step 1: Put the AOI into a GeoDataFrame to easily manage CRS
    aoi_gdf = gpd.GeoDataFrame([{'geometry': aoi_geometry}], crs=aoi_crs)
    grid_crs = grid_definition["crs"]

    # Step 2: Transform the AOI to the grid's CRS
    aoi_in_grid_crs = aoi_gdf.to_crs(grid_crs)
    
    # Get the single geometry object after transformation
    aoi_geom_transformed = aoi_in_grid_crs.geometry.iloc[0]

    # Step 3: Get the bounding box of the transformed AOI
    minx, miny, maxx, maxy = aoi_geom_transformed.bounds
    
    # Step 4: Calculate the range of grid cell indices covering the bounding box
    # This uses floor division to find the index of the cell containing a coordinate
    origin_x = grid_definition["origin_x"]
    origin_y = grid_definition["origin_y"]
    cell_w = grid_definition["cell_size_x"]
    cell_h = grid_definition["cell_size_y"]

    col_start = int((minx - origin_x) // cell_w)
    col_end = int((maxx - origin_x) // cell_w)
    row_start = int((miny - origin_y) // cell_h)
    row_end = int((maxy - origin_y) // cell_h)

    # Step 5: Iterate through candidate cells and perform precise intersection tests
    intersecting_cell_ids = []
    for col in range(col_start, col_end + 1):
        for row in range(row_start, row_end + 1):
            # Calculate the lower-left corner of the current grid cell
            cell_ll_x = origin_x + col * cell_w
            cell_ll_y = origin_y + row * cell_h
            
            # Create a shapely geometry for the grid cell
            cell_box = box(cell_ll_x, cell_ll_y, cell_ll_x + cell_w, cell_ll_y + cell_h)

            # Perform the precise intersection test
            if aoi_geom_transformed.intersects(cell_box):
                # Step 6: If it intersects, calculate the final ID tuple
                
                # a) Find the geometric reference point (e.g., lower-left, center)
                geom_ref_x = cell_ll_x + grid_definition["cell_id_ref_point_offset_x"]
                geom_ref_y = cell_ll_y + grid_definition["cell_id_ref_point_offset_y"]
                
                # b) Scale the reference point to get the output ID component
                output_x = geom_ref_x / grid_definition["output_id_scale_x"]
                output_y = geom_ref_y / grid_definition["output_id_scale_y"]
                
                # c) Cast to integer if required
                if grid_definition["output_id_type"] == "integer":
                    output_x = int(output_x)
                    output_y = int(output_y)
                
                intersecting_cell_ids.append((output_x, output_y))

    # Step 7: Return the list of unique IDs
    return intersecting_cell_ids