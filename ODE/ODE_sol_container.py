# -*- coding: utf-8 -*-
"""
Last update: 2021-08-11
Moduel information
A container to solve SciPy ODE solution moduels. 
The parameter range information should be given as below, and the directory should be 

Use with /PBBP_UNIST/Samplings/random_parameters.py

Required module. 
    pandas
    matplotlib
    copy
    os
    scipy 
    PBBP_UNIST/make_dirs

Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""

"""
Develop Note. 
Things to do. 
"""


import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
from PBBP_UNIST.File_mange import read_write
import copy 
import os 

class ODE_solution():
    num_simulation = 0
    
    ### --- a container for ODE solutions. 
    def __init__(self, default_output = True, *args, **kwargs):
        """
        args --> function
        kwargs --> 
        key     : number of the function (begin with 0)
        item    : dictionary with { "name" : function name, "args" : (argument tuples) } 
        """
        self.t  = None
        self.dt = None
        self.sol    = {}
        self.sol_ic = {}
        self.t_end  = None
        self.t_begin    = None
        self.para_dict  = {}
        self.sol_type   = None
        self.sol_numbering  = {}
        self.output_dict = {}
        
        if default_output: 
            self.output_dict.update({
                "t_begin"   : self.t_begin,
                "t_end"     : self.t_end,
                "dt"        : self.dt                
            })
        
        assert len(args) == len(kwargs.keys()), "number of function and the number of the function arguments does not met. # of function {:02d}, # of the function arguments {:02d}".format(len(args), len(kwargs.keys()))
            
        for key, kw_dict in kwargs.items():
            self.output_dict[kwargs["name"]] = args[key](*kwargs["args"])
        #
    #

    def save_to_csv(self, result_dir = "./", save_items = "all", **kwargs): 
        ### --- moduel information
        # A moudle to save data.
        # input 
        # result_dir    : (str) A file directory path with the file name. 
        # save_items    : (str, lis or set) If string "all" is given, save all items. Else, items in the list or set is saved. 
        # case_id       : (int) A case id given to the profile. 
        # 
        # output
        # (file)    : Data file is saved in CSV file format.
        ### --- end

        out_dict_temp = {} 
        
        if save_items == "all": 
            out_dict_temp.update(self.output_dict)

        if not os.path.isfile(result_dir):
            pd.DataFrame(out_dict_temp, index = [0]).to_csv(result_dir, index = False)
        else :
            pd.DataFrame(out_dict_temp, index = [0]).to_csv(result_dir, mode = "a", header = False, index = False)
        # 
    #

    def plot_png(self, ax, frac_beg = 0.5, frac_end = 1, **kwargs):
        ### --- moduel information
        # A moudle to save profiles.
        # input 
        # ax            : axes object
        # frac_beg      : (float) A number between 0 - 1. The beginning time point of plotting. 
        # frac_beg      : (float) A number between 0 - 1. The end time point of plotting. 
        # 
        # output
        # (file)    : Data file is saved in CSV file format.
        ### --- end

        
        assert self.t != None, "Solution not saved yet"

        index_beg = int(len(self.t)*frac_beg)
        index_end = int(len(self.t)*frac_end)
        
        for elem, data in self.sol.items():
            ax.plot(self.t[index_beg:index_end] , data[index_beg:index_end], label = elem)
        #
        
        return ax
    #
#
