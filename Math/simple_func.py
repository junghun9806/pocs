# -*- coding: utf-8 -*-
""" 
Last update: 2022-05-10
Module information

Required module. 
    Numba
    
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
modify to_distance_matrix using pivot table function in pandas. 
"""
from numba import njit

@njit 
def delta(a, b): 
    if a == b:
        return 1 
    else : 
        return 0 
    #
# 

