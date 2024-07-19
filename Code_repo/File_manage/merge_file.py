# -*- coding: utf-8 -*-
""" 
Last update: 2022-01-17
Module information

Required module. 
    
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
"""

def merge_csv(fname_list, fname_new = "newfile", remove_header=True):
    with open(fname_new, "a") as f_write:
        for idx, fname in enumerate(fname_list):
            with open(fname, "r") as file: 
                if idx > 0 and remove_header: 
                    file.readline()
                #
                f_write.write(file.read())
            #
        #
    #
#