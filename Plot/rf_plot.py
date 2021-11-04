import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def rankplot_jh(ax, data, beg=1, Normalize = False, mode = "htol", **kwargs):
    """
    Draw rank frequecny plot
    
    ax              : draw figure to matplotlib object ax.
    data            : (iterable) data
    beg             : beginning of the rank plot. 
    Nomralize       : False. If True, Normalize with highest rank = 1. if Normalize is True, beg is automatically set to 1. 
    mode            : "htol" highest to lowest, "ltoh" lowest to highest.
    
    code written by Junghun Chae 
    Contact: 
    junghun98@unist.ac.kr
    wjdgnswkd612@gmail.com
    """
    
    arr = list(data)
    arr.sort(reverse= True if mode == "htol" else False )
    
    length = len(arr)
    
    if Normalize: 
        x = [ (i + 1) / length for i in range(length)]
    else : 
        x = [ (i + beg) for i in range(length)]
    #
    
    ax.plot(x, arr, kwargs)
    
    return ax 
#