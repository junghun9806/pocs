# -*- coding: utf-8 -*-
""" 
Last update: 2022-01-20
Module information

Required module. 
    NumPy
    Numba
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
"""

import numpy as np
from numba import njit 
from numba.typed import List

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


