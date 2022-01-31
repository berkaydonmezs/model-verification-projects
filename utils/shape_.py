import rioxarray
import geopandas as gpd
from utils import proj_
from shapely.geometry import mapping
from cartopy.io.shapereader import Reader

turkey_shape = Reader(r'data/shapefile/turkey_provinces.shp')
turkey_shape_df = gpd.read_file(r'data/shapefile/turkey_provinces.shp')

def clip_turkey_shape(data, lat_coord_name='latitude', lon_coord_name='longitude'):

    data = data.rio.write_crs(proj_.basic_crs_info_2)
    data = data.rio.set_spatial_dims(y_dim=lat_coord_name, x_dim=lon_coord_name)
    
    data = data.rio.clip(turkey_shape_df.geometry.apply(mapping), data.rio.crs, drop=True, invert=False)
    return data
    