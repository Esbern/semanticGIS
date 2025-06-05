
# %% 
import os
import subprocess
import yaml
import rasterio
from rasterio.errors import RasterioIOError

# %%

def read_config(config_path):
    """Reads configuration from a YAML file."""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}")
        exit()
    except yaml.YAMLError as e:
        print(f"Error parsing YAML config file: {e}")
        exit()

#%% 
def create_cog(config):
    """
    Converts a standard TIFF to a Cloud Optimized GeoTIFF (COG)
    based on configurations from the YAML file.
    """
    input_tif_path = config['input_tif_path']
    output_cog_path = config['output_cog_path']
    cog_options = config['cog_creation_options']
    overview_levels = config['overview_generation']['levels']
    resampling_method = config['overview_generation']['resampling_method']

    print(f"Starting COG conversion for: {input_tif_path}")
    print(f"Output COG will be saved to: {output_cog_path}")

    if not os.path.exists(input_tif_path):
        print(f"Error: Input file not found at {input_tif_path}")
        return

    # Determine nodata value from input TIFF
    nodata_value = None
    try:
        with rasterio.open(input_tif_path) as src:
            nodata_value = src.nodata
            if nodata_value is None:
                print("Warning: No Nodata value found in input TIFF. Consider adding one for better compression and data integrity.")
                # You might want to uncomment and set a default nodata if you know it, e.g.,
                # nodata_value = -9999.0
    except RasterioIOError as e:
        print(f"Error opening input TIFF with rasterio: {e}")
        return

    # Build gdal_translate command
    gdal_translate_cmd = [
        'gdal_translate',
        input_tif_path,
        output_cog_path,
        '-of', 'COG',
    ]

    # Add creation options from YAML
    for key, value in cog_options.items():
        gdal_translate_cmd.extend(['-co', f'{key}={value}'])

    if nodata_value is not None:
        gdal_translate_cmd.extend(['-a_nodata', str(nodata_value)])

    print(f"\nRunning gdal_translate: {' '.join(gdal_translate_cmd)}")
    try:
        subprocess.run(gdal_translate_cmd, check=True, capture_output=True, text=True)
        print("gdal_translate completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during gdal_translate:\n{e.stdout}\n{e.stderr}")
        return
    except FileNotFoundError:
        print("Error: gdal_translate not found. Ensure GDAL is installed and in your PATH.")
        return

    # Build gdaladdo command for overviews
    gdal_addo_cmd = [
        'gdaladdo',
        '-r', resampling_method,
        output_cog_path
    ] + [str(level) for level in overview_levels]

    print(f"\nRunning gdaladdo: {' '.join(gdal_addo_cmd)}")
    try:
        subprocess.run(gdal_addo_cmd, check=True, capture_output=True, text=True)
        print("gdaladdo completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during gdaladdo:\n{e.stdout}\n{e.stderr}")
        return
    except FileNotFoundError:
        print("Error: gdaladdo not found. Ensure GDAL is installed and in your PATH.")
        return

    print(f"\nCOG conversion complete for {output_cog_path}")

# --- Main Execution ---
if __name__ == "__main__":
    # Path to your YAML configuration file
    config_file = 'config.yml'

    # Read the configuration
    app_config = read_config(config_file)

    # Run the COG conversion
    create_cog(app_config)