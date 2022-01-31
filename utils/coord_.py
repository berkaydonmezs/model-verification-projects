def subset_turkey_coords(data, lat_coord_name='latitude', lon_coord_name='longitude'):
    if data[lat_coord_name][0] > data[lat_coord_name][1]:
        query_dict = {lat_coord_name:slice(42,36),
                      lon_coord_name:slice(26,45)}
    else:
        query_dict = {lat_coord_name:slice(36,42),
                      lon_coord_name:slice(26,45)}
        
    _data_turkey = data.sel(query_dict)
    return _data_turkey