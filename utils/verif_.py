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

def tab_accuracy(hits, correct_negatives, total):
    """
    Calculates accuracy from the contingency table
    """
    
    return np.round((hits+correct_negatives)/total, 3)

def tab_bias_score(hits, false_alarms, misses):
    """
    Calculates bias score from the contingency table
    """
    return np.round((hits+false_alarms)/(hits+misses), 3)

def tab_POD(hits, misses):
    """
    Calculates probability of detection (POD) from the contingency table
    """
    
    return np.round(hits/(hits+misses), 3)

def tab_FAR(hits, false_alarms):
    """
    Calculates false alarm ratio (FAR) from the contingency table
    """
    
    return np.round(false_alarms/(hits+false_alarms), 3)

def tab_POFD(correct_negatives, false_alarms):
    """
    Calculates probability of false detection (false alarm rate) (POFD) from the contingency table
    """
    
    return np.round(false_alarms/(correct_negatives+false_alarms), 3)

def tab_success_ratio(hits, false_alarms):
    """
    Calculates success ratio from the contingency table
    """
    
    return np.round(hits/(hits+false_alarms), 3)

def tab_threat_score(hits, misses, false_alarms):
    """
    Calculates threat score from the contingency table
    """
    
    return np.round(hits/(hits+misses+false_alarms), 3)

def tab_equitable_threat_score(hits, hits_random, misses, false_alarms):
    """
    Calculates equitable threat score from the contingency table
    """
    
    return np.round((hits-hits_random)/(hits+misses+false_alarms-hits_random), 3)

def tab_HK(hits, correct_negatives, misses, false_alarms):
    """
    Calculates Hanssen and Kuipers discriminant (Peirce's skill score) from the contingency table
    """
    
    return np.round((hits/(hits+misses)) - (false_alarms/(false_alarms+correct_negatives)), 3)