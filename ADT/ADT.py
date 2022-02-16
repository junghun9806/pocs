# -*- coding: utf-8 -*-
""" 
Last update: 2022-02-16
Module information

Arbitrary Data Types

Required module. 
    copy
    
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
"""

import copy

def nested_dict(keys, init = 0):
    """
    init : initial value for the deepest dictionary elements
    args : nested lists of dictionary keys. 
    """
    
    depth = len(keys)
    
    assert depth > 0, "the length of the keys should be larger than 1"
    for i in keys: 
        assert type(i) == list, "type of element should be list"
        assert len(i) > 0, "the number of element should be more or equal than one."
    # 
    
    temp_dict = dict()
    dict_t = {}
    for i in range(len(keys)):
        dict_new = {}
        deepest = True
        for key in keys[-i]:
            if deepest : 
                dict_t[key] = init
                deepest = False
            else : 
                dict_new[key] = copy.deepcopy(dict_t)
                dict_t = copy.deepcopy(dict_new)
            #
        #
    #
    
    return dict_t
#