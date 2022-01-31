import cartopy
import rioxarray
import numpy as np

def interpolate_xy(data, lon_name, lat_name, interp_size):
    
    # new lon and lat info
    new_lon = np.linspace(data[lon_name][0], data[lon_name][-1], len(data[lon_name]) * interp_size)
    new_lat = np.linspace(data[lat_name][0], data[lat_name][-1], len(data[lat_name]) * interp_size)
    
    # interpolate the data
    new_parameters = {lon_name:new_lon,
                      lat_name:new_lat}
    interp_data = data.interp(new_parameters)
    
    return interp_data