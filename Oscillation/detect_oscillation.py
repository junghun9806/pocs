"""
1. Peak to peak time difference. 
2. Fold change of peak 1-eps to 1+eps. Epsilon value should be conservative. And not a strange number. 
3. Minimum threshold for alpha Value. 
4. Peak value of A_bar comapare with 1. Always be critical debugging. 
"""

from scipy.signal import find_peaks
import numpy as np

def detect_oscillation(t, y, frac = 0.5):
    ### ---- module information. 
    # A module for detecting oscillations. ###
    # input
    # t     : (list) Time series for y. 
    # y     : (list) Data for time series t. 
    # frac  : (float) 0-1. The fraction where the sustained oscillation begins. 
    #  
    # output 
    # ### --- end.    
    index = int(len(t) * frac)

    t = t[index : ]
    y = y[index : ]

    eps_period  = 0.05
    eps_height  = 0.05
    min_alpha   = 0.2

    criteria_1 = False
    criteria_2 = False
    criteria_3 = False 

    criteria_dict = {}

    # Detect peaks 
    peak_t_list, peak_dict = find_peaks(y)

    # Criteria 1 
    # disgard the first time difference. 
    t_dif_list = np.diff(peak_t_list[1:])

    min_period = min(t_dif_list)
    max_period = max(t_dif_list)

    if max_period / min_period < 1 + eps_period : 
        criteria_1 = True 
    # 

    criteria_dict["c1"] = {
        "status" : criteria_1,
        "value"  : max_period / min_period -1
    }

    # Criteria 2 
    peak_height_list = peak_dict["height"][1:]
    min_peak = min(peak_height_list)
    max_peak = max(peak_height_list)

    if max_peak / min_peak < 1 + eps_height :
        criteria_2 = True
    #

    criteria_dict["c1"] = {
        "status" : criteria_2,
        "value"  : max_peak / min_peak -1
    }

    # Criteria 3 
    trough_t_list, trough_dict = find_peaks(y)
    trough_height_list = trough_dict["height"][1:]
    mean_peak   = np.mean(peak_height_list[-2:])
    mean_trough = np.mean(trough_height_list[-2:])
    alpha = 1 - mean_trough/mean_peak

    if alpha >= min_alpha : 
        criteria_3 = True

    criteria_dict["c1"] = {
        "status" : criteria_3,
        "value"  : alpha
    }

    criteria_all = True
    for cri in criteria_dict:
        criteria_all = criteria_all and cri["status"]

    return [criteria_all, criteria_dict]
#
