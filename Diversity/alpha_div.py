# -*- coding: utf-8 -*-
""" 
Last update: 2022-01-17
Moduel information
df_sp : pandas dataframe 

df_sp should contain a column with header "index" and its relative abundaces (%). 

Required module. 
    Pandas
    NumPy

Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
"""

import pandas as pd 
import numpy as np 

def species_abundance(df_sp : pd.DataFrame):
    return len(df_sp)
#

def shannon_rel(df_sp : pd.DataFrame, index : str):
    res = 0
    for i in df_sp.index:
        res += -1 * df_sp[index][i]/100 * np.log(df_sp[index][i]/100)
    #
    return res 
#

def simpson(df_sp : pd.DataFrame, index : str): 
    res = 0
    for i in df_sp.index:
        res += (df_sp[index][i]/100)**2
    #
    return 1 - res
#