# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:09:11 2021

@author: gaoyuan
"""


def get_min_odd(numbers,min_n=9999):
    if len(numbers) > 0:
        tmp = numbers[-1]
        if tmp % 2 != 0 and tmp < min_n:
            min_n = tmp
            numbers.pop()
            return get_min_odd(numbers,min_n)
        else:
            return get_min_odd(numbers[:-1],min_n)
    else:
        return min_n
        
    