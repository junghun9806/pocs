# -*- coding: utf-8 -*-
""" 
Last update: 2022-01-20
Module information

Required module. 
    NumPy
    Numba
    Pandas 
    
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
modify to_distance_matrix using pivot table function in pandas. 
"""

from itertools import product

import pandas as pd
import numpy as np

from numba import njit 


@njit
def to_condensed_distance(X:np.array):
    length = len(X)
    
    condensed = []
    
    for i in range(length):
        for j in range(i+1, length):
            condensed.append(X[i][j])
        #
    # 
    
    return condensed
#

def to_distance_matrix(dist_df: pd.DataFrame, dist_index : str, *args : list, nonval = 0):

    """    
    The column should have args[0]+"1" and args[0]+"2", args[1] + "1" and args[1] + "2" formatted strings. 
    args elements should not have "_"
    For example 
    if args = ["alpha", "beta"]
    then the pandas Dataframe should have the following columns. 
    "alpha1", "alpha2", "beta1", "beta2", "<dist_index>"
    
    This function generates 2 dictionaries and a 2D array. 
    A dictionary have key of "alpha"+"_"+"beta" and its value of 0 to n depending on the length of the distance matrix. 
    A dictionary that has opposite values of the other one. key -> value, value -> key. 
    A 2D array containing "dist_index" values. 
    
    nonval = when the corresponding distance value does not exists, nonval is put to the distance matrix.
    """
    
    var_len = len(args)
    assert var_len > 0, "number of arguments should be larger than 0."
    
    mat_len = 1
    
    for arg in args:
        if type(arg) == str:
            assert "_" not in arg, "'_' should not be in the <args>."
        #
        
        mat_len *= len(set(dist_df[arg + "1"]))
    # 
    
    id2key = dict()
    key2id = dict()
    
    var_set_list = []
    for arg in args:
        set_temp = set(dist_df[arg + "1"])
        set_temp.update(set(dist_df[arg + "2"]))
        var_set_list.append(set_temp)
    
    id_t = 0
    for arg_comb in product(*var_set_list):
        index_t = ""
        for arg_t in arg_comb:
            index_t += str(arg_t) + "_"
        # 
        
        # remove "_" at last
        index_t = index_t[:-1]
        
        id2key[id_t] = index_t
        key2id[index_t] = id_t
        id_t += 1 
    # 
    
    comb_numb = len(key2id)
    
    dist_matrix = [[nonval for __ in range(comb_numb)] for _ in range(comb_numb)]
    
    for rows in dist_df.iterrows():
        data = rows[1]
        
        var1 = str(data[args[0] + "1"])
        var2 = str(data[args[0] + "2"])
        for i in range(1, var_len):
            var1 += "_" + str(data[args[i] + "1"])
            var2 += "_" + str(data[args[i] + "2"])
        #
        
        if dist_matrix[key2id[var1]][key2id[var2]] != nonval: 
            print("WARNING :: possible overwritting")
        # 
        
        dist_matrix[key2id[var1]][key2id[var2]] = data[dist_index]
    #
    return dist_matrix, id2key, key2id
#

