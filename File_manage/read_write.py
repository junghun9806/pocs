# -*- coding: utf-8 -*-
""" 
Last update: 2022-01-17
Module information

Required module. 
    os
    pickle
    
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
"""

import os 
import pickle

def make_dir(file_path: str) -> None:
    try : 
        os.makedirs(file_path)
    except : 
        pass
    #
#

def pickle_load(fname : str) -> None:
    with open(fname, "rb") as fr: 
        obj = pickle.load(fr)
    #
    return obj
#

def pickle_dump(f_dir : str, fname : str, obj) -> None:
    make_dir(f_dir)
    
    with open(f_dir + "/" + fname, "wb") as fw: 
        pickle.dump(obj, fw)
    #
    return None
#

