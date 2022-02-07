# -*- coding: utf-8 -*-
""" 
Last update: 2022-01-17
Module information

General info: Draw seaborn figure and adjust

Required module. 
    os
    pickle
    seabron
    matplotlib
    
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
"""

import pandas as pd
import seaborn as sns 

def draw_relplot(
    data : pd.DataFrame, 
    save_dir : str, 
    xlabel_dict = {} , 
    ylabel_dict = {} ,  
    x_lim = {} ,
    y_lim = {} ,
    
    **kwargs_sns):
    
    graph = sns.relplot(data=data, **kwargs_sns)
    
    #graph.ax.set_xticklabels(graph.ax.get_xticklabels(), rotation = 45, ha = "right")
    graph.ax.set_xticklabels(graph.ax.get_xticklabels(), **xlabel_dict)
    graph.ax.set_yticklabels(graph.ax.get_yticklabels(), **ylabel_dict)
    graph.ax.set_ylim(**y_lim)
    graph.ax.set_xlim(**x_lim)
    graph.savefig(save_dir, dpi=300)

    return graph.ax



def draw_relplot(
    data : pd.DataFrame, 
    save_dir : str, 
    xlabel_dict = {} , 
    ylabel_dict = {} ,  
    x_lim = {} ,
    y_lim = {} ,
    
    **kwargs_sns):
    
    graph = sns.relplot(data=data, **kwargs_sns)
    
    #graph.ax.set_xticklabels(graph.ax.get_xticklabels(), rotation = 45, ha = "right")
    graph.ax.set_xticklabels(graph.ax.get_xticklabels(), **xlabel_dict)
    graph.ax.set_yticklabels(graph.ax.get_yticklabels(), **ylabel_dict)
    graph.ax.set_ylim(**y_lim)
    graph.ax.set_xlim(**x_lim)
    graph.savefig(save_dir, dpi=300)

    return graph.ax