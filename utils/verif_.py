import cartopy
import rioxarray
import numpy as np

def get_anomaly(data, climatology, anomaly_type, resample_by='mean'):
    """
    Calculate the anomaly of the data given a climatology
    data: data for which the anomaly values are to be calculated (xarray obj)
    climatology: data which will be used as a reference in anomaly calculation (xarray obj)
    anomaly_type: calculate "anomaly_type" anomaly (e.g., monthly anomaly where anomaly_type='month')
    resample_by: resampling method of the climatology data. Use mean or sum depending on the utilized data variable
    
    Returns data anomaly having the same spatial and temporal dims as 'data'
    """
    
    if resample_by == 'mean':
        data_mean = climatology.groupby(fr"time.{anomaly_type}").mean(dim='time')
    elif resample_by == 'sum':
        data_mean = climatology.groupby(fr"time.{anomaly_type}").sum(dim='time')   
    
    data_anom = data.groupby(fr"time.{anomaly_type}") - data_mean
    
    return data_anom