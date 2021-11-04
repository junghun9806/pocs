import pandas as pd 

def rankplot_jh(ax, data, beg=1, Normalize = False, reverse = False):
    """
    Draw rank frequecny plot
    
    ax              : draw figure to matplotlib object ax.
    data            : (iterable) data
    beg             : beginning of the rank plot. 
    Nomralized      : False. If True, Normalize with highest rank = 1. 
    reverse = False : highest to Loweest
    
    code written by Junghun Chae 
    Contact: 
    junghun98@unist.ac.kr
    wjdgnswkd612@gmail.com
    """
    
