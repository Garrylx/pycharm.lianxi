# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:33:14 2021

@author: gaoyuan
"""

def binary_search(values,item,left=0,right=0):
    mid = len(values)//2
    if left <= right:
        right  = len(values)-1
        print(str(values[:mid])+" "+str(values[mid])+" "+str(values[mid+1:]))
        if item == values[mid]:
            return True
        elif item < values[mid]:
            right = mid-1
            return binary_search(values[:right+1],item,left,right)
        elif item > values[mid]:
            left = mid+1
            return binary_search(values[left-1:],item,left,right)
    else:
        return False
    
test_list = list(range(40))
print(binary_search(test_list, 3))

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 20 [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 10 [11, 12, 13, 14, 15, 16, 17, 18, 19]
#[0, 1, 2, 3, 4] 5 [6, 7, 8, 9]
#[0, 1] 2 [3, 4]
#[3] 4 []
#[] 3 []
# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binary_search(test_list, 3))
# print(binary_search(test_list, 13))