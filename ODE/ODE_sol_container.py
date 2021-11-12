# -*- coding: utf-8 -*-
"""
Last update: 2021-08-11
Moduel information
A container to solve SciPy ODE solution moduels. 
The parameter range information should be given as below, and the directory should be 


Required module. 
    pandas
    matplotlib
    copy
    os

Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""

"""
Develop Note. 
Things to do. 
    1. make a method which return pandas DataFrame form of parameters. 
"""


import matplotlib.pyplot as plt
import pandas as pd 
import copy 
import os 

class ODE_solution():
    num_simulation = 0
    
    ### --- a container for ODE solutions. 
    def __init__(self):
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
    #

    def save_to_csv(self, result_dir = "./", save_items = "all", ): 
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

        key_orders = []

        if save_items == "all": 
            out_dict_temp = copy.deepcopy(self.output_dict)
            key_orders.extend(list(self.output_dict.keys()))
        else : 
            for item in save_items: 
                out_dict_temp[item] = self.output_dict[item]
            key_orders.extend(list(save_items))

        for para in self.para_dict.keys(): 
            out_dict_temp[para] = self.para_dict[para]
            key_orders.append(para)
        #

        key_orders.insert(0, "case_id") 
        out_dict_temp["case_id"] = case_id

        key_orders.insert(1, "sol_type") 
        out_dict_temp["sol_type"] = self.sol_type

        if not os.path.isfile(result_dir):
            pd.DataFrame(out_dict_temp, index = [0]).to_csv(result_dir, columns=key_orders, index = False)
        else :
            pd.DataFrame(out_dict_temp, index = [0]).to_csv(result_dir, columns=key_orders, mode = "a", header = False, index = False)
        # 
    #

    def plot_png(self, result_dir = "./", frac_beg = 0.5, frac_end = 1, dpi=300, case_id = 0):
        ### --- moduel information
        # A moudle to save profiles.
        # input 
        # result_dir    : (str) A file directory path with the file name. 
        # frac_beg      : (float) A number between 0 - 1. The beginning time point of plotting. 
        # frac_beg      : (float) A number between 0 - 1. The end time point of plotting. 
        # dpi           : (int) DPI value to save png file.
        # case_id       : (int) A case id given to the profile. 
        # 
        # output
        # (file)    : Data file is saved in CSV file format.
        ### --- end
        save_dir = result_dir + "{:08}_".format(case_id) + self.sol_type + ".png"

        if not self.output_dict["solution_success"] == 0:
            return 
        #

        index_beg = int(len(self.t)*frac_beg)
        index_end = int(len(self.t)*frac_end)
        for elem, data in self.sol.items():
            plt.plot(self.t[index_beg:index_end] , data[index_beg:index_end], label = elem)
        plt.title(elem)
        plt.grid()
        plt.legend()
        plt.savefig(save_dir, dpi = dpi)

        plt.clf()
        plt.cla()
        plt.close("all")
    #
#
