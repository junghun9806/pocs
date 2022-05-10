# -*- coding: utf-8 -*-
""" 
Last update: 2022-01-21
Module information

General info: decorators 

Required module. 
    
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
"""
import time

def measure_time(func):
    def decorated(param):
        x = time.time()
        res = func(**param)
        dt = time.time()-x
        return dt, res
    #
    return decorated
# 