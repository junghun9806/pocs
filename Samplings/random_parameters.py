# -*- coding: utf-8 -*-
"""
Last update: 2021-08-11
Moduel information
Generate parameter sets with given parameter range. 
The parameter range information should be given as below, and the directory should be 
in the "__init__" argument para_range_dir. 

Required module. 
    pandas
    os
    random

Input file.
    First 3 columns are required. 

    CSV format file
    names,min,max,msb2012_min,msb2012_max,unit,Note
    ao,0.1,10,0.33,102.9,,
    at,0.1,10,0.53,8.907,,
    ah,0.1,10,0.1,100,,
    bo,0.1,10,0.369,1.51,,
    bt,0.1,10,0.07,3.537,,
    bh,0.1,10,0.07,3.537,,
    A,0.1,10,0.01,100,,
    Kd,0.00001,0.0001,0.00001,1,,
    Kd_TF,1,100,1,1000,,
    V,100,1000,100,1000,,
    K_dlt,0.01,0.1,,,,
    K_delta,1,10,,,,
    k1,1,100,,,,

Code written by Junghun Chae. 
Contact: 
junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""

"""
Develop Note. 
Things to do. 
    1. make version for multiprocessing
    

"""

import pandas as pd
import os
import scipy.stats as stats


class Parameter():
    ### --- class Parameter 
    # A class to generate random numbers. 
    # Used for parameter samplings.
    # ### --- end. 
    def __init__(self, para_range_dir, parameter_dir, scale = "linear",  **kwargs):
        ### --- constructor 
        # input 
        # para_range_dir    : (str) A directory where the parameter sampling rane is recorded. 
        # parameter_dir     : (str) A dicrectory where it can save the sampled parameters. 
        # scale             : (str) Sampling method. "linear", "logarithmic" are possilbe input.  
        
        # kwargs : 
        # "log_set" : set of parameters to sample in log scale. 
        # "n_sample" : total number of sampling. default is 1000. 
        ### --- end. 
        self.para_range_dir = para_range_dir
        self.parameter_dir  = parameter_dir
        
        assert os.path.isfile(para_range_dir), "Parameter Range file not exists"
        assert scale in ["log", "linear"], "scale should be log or linear"
        ref_table = pd.read_csv(para_range_dir).set_index("names")
        
        
        if "log_set" in kwargs.keys():
            self.log_set = kwargs["log_set"]
        else : 
            self.log_set = set()
        #
        if "n_sample" in kwargs.keys():
            self.N_max = kwargs["n_sample"] * 100
        else : 
            self.N_max = 1000 * 100
        # 
        
        parameters = ref_table.index.values
        self.ref_table = ref_table 
        self.parameter_list = parameters
        self.scale = scale
        self.case_id_set = set()
    #

    def generate_parameters(self, parameter_dir = None, save=False, **kwargs):
        ### --- generate parameters 
        # input 
        # parameter_dir : (str) The name of file to save the parameters. 
        # save          : (boolean) Whether to save the param
        ### --- end. 
        
        ### KWARGS BEGIN
        if "log_set" in kwargs.keys():
            self.log_set = kwargs["log_set"]
        else : 
            self.log_set = set()
        #
        if "n_sample" in kwargs.keys():
            self.N_max = kwargs["n_sample"] * 100
        else : 
            self.N_max = 1000 * 100
        # 
        ### KWARGS END
        
        
        para_dict = {}
        new = False
        
        if parameter_dir == None:
            parameter_dir = self.parameter_dir

        while (not new):
            case_id = stats.randint.rvs(0, self.N_max)
            if not case_id in self.case_id_set : 
                self.case_id_set.add(case_id) 
                new = True 
            # 
        #
        
        para_dict["ID"] = case_id 
        for para in self.parameter_list:
            if self.scale == "linear" : 
                if para in self.log_set: 
                    para_dict[para] = stats.loguniform.rvs(self.ref_table.loc[para]["min"], self.ref_table.loc[para]["max"])
                else : 
                    para_dict[para] = stats.uniform.rvs(self.ref_table.loc[para]["min"], self.ref_table.loc[para]["max"])
                #
            elif self.scale == "log": 
                para_dict[para] = stats.loguniform.rvs(self.ref_table.loc[para]["min"], self.ref_table.loc[para]["max"])
            #
        #
        
        if save:
            if not os.path.isfile(parameter_dir):
                pd.DataFrame(para_dict, index = [0]).to_csv(parameter_dir, index = False)
            else :
                pd.DataFrame(para_dict, index = [0]).to_csv(parameter_dir, mode = "a", header = False, index = False)
            # 
        #
        return para_dict
    #
#