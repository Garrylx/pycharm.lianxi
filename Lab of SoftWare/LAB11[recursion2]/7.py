# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:26:44 2021

@author: gaoyuan
"""

def get_gcd(m, n):
    if m < n:
        m , n = n , m
    n1 = m % n
    if n1 != 0:
        return get_gcd(n, n1)
    else:
        return n
print(get_gcd(100, 70))