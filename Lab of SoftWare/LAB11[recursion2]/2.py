# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:16:01 2021

@author: gaoyuan
"""

def get_sum_digits(number):
    number = str(number)
    if len(number) > 0:
        tmp = number[0]
        return int(tmp) + get_sum_digits(number[1:])
    else:
        return 0