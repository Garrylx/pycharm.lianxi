# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:48:28 2021

@author: gaoyuan
"""

def get_merge_list(list_of_lists):
    if len(list_of_lists) > 0:
        f_lists = list_of_lists[0]
        lists = list_of_lists[1:]
        return f_lists + get_merge_list(lists)
    else:
        return []
        
    