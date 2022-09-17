# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:54:15 2021

@author: gaoyuan
"""

def get_sum_ascii(word):
    if len(word) > 0:

        tmp = word[0]
        word = word[1:]
        return ord(tmp) + get_sum_ascii(word)
    
    return 0
print(get_sum_ascii("This is a Test"))
    