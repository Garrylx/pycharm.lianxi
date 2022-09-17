# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:42:03 2021

@author: gaoyuan
"""

def collatz(x):
    print(int(x))
    if x == 1:
        return x
    elif x % 2 == 0:
        return collatz(x/2)
    else:
        return collatz(x*3+1)
    
collatz(12)