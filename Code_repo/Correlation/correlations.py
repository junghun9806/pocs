# -*- coding: utf-8 -*-
""" 
Last update: 2022-01-17
Module information

correlation measures

Required module. 
    math
    
Code written by Junghun Chae. 
Contact: junghun98@unist.ac.kr 
wjdgnswkd612@gmail.com
"""
"""
Develop Note. 
Things to do. 
"""

import math

def sign(x):
    return math.copysign(1, x)
#

# ### kendall_tau function
### --- kendall tau module --- ### 
#   for given two list 
# [a, b, c, d, e] 
# [f, g, h, i, j]
# then the index would be --> 1, 2, 3, 4, 5
# then for all pair of index (1, 2), (1, 3) *** (4, 5) do the following process
# let U = 0, D = 0 
# let (1, 2) is chosen then  
# if a > f, 
#   if b > g : then U += 1, D += 1
#   if b < g : then U -= 1, D -= 1
#   if b == g : then U += 0, D += 1
# if a == f, 
#   if b != g : then U += 0, D += 1 
#   if b == g : then U += 1, D += 1 
# where kendall_tau value is U/D
### --- end --- ### 

def kendall_tau(x, y):
    assert len(x) == len(y), "two list length not equal"
    assert min(x) >= 0, f"minimum value of list x is negative: {min(x)}"
    assert min(y) >= 0, f"minimum value of list y is negative: {min(y)}"
    
    U = 0
    D = 0 
    length = len(x)

    for i in range(length):
        for j in range(length):
            if i == j: 
                continue 
            #
            if i > j : 
                continue
            #
            dif0 = x[i] - x[j]
            dif1 = y[i] - y[j]

            if dif0 == 0: 
                if dif1 ==0  : 
                    U += 0
                    D += 1
                else :
                    U += 0
                    D += 1
                #
            else:
                if dif1 == 0: 
                    U += 0
                    D += 1
                #
                elif sign(dif0) == sign(dif1): 
                    U += 1 
                    D += 1 
                else :
                    U -= 1
                    D += 1  
                #
            #
        #
    #
    if D == 0:
        return float("NaN")
    return float(U) / float(D)
# --- func end 