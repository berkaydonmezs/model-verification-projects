import cartopy
import rioxarray
import numpy as np

basic_crs_info_1 = cartopy.crs.LambertConformal(35.75154, 39.49263, standard_parallels=(20, 60)).proj4_params
basic_crs_info_2 = cartopy.crs.PlateCarree().proj4_params

def check_dim_consistency(data1, data2):
    assert data1.dims == data2.dims, "data dims do not match, consider matching"
    print("data dims match, you can continue")
    
def reproject_match_rio(data, match_data, data_proj, match_data_proj):
    """
    reproject data to match the spatial structure of match data
    """
    data = data.rio.write_crs(data_proj)
    match_data = match_data.rio.write_crs(match_data_proj)
        
    return data.rio.reproject_match(match_data)

def match_latlon_dims(data):
    """
    match y to latitude; x to longitude
    """
    return data.rename({'y': 'latitude',
                        'x': 'longitude'})