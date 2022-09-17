# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:35:49 2021

@author: gaoyuan
"""

def get_odds_list(numbers,lists=None):
    if lists == None:
        lists = []
    else:
        pass
    if len(numbers) > 0:
        tmp = numbers[0]
        if tmp % 2 != 0:
            lists.append(tmp)
            numbers = numbers[1:]
            return get_odds_list(numbers,lists)
        else:
            return get_odds_list(numbers[1:],lists)
    else:
        return lists
    
print(get_odds_list([2, 3, 5, 6]))


print(get_odds_list([9, 5, 15, 11, 23]))


print(get_odds_list([2, 4, 6, 8]))


print(get_odds_list([2, 3, 1, 5, 6, 9]))