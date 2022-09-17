# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:51:42 2021

@author: gaoyuan
"""


    

def join_multiply(l1,l2,fl,fl2=None):
    if fl2 == None:
        fl2 = []
    if len(l2) > 0 and len(l1) > 0:
        calu = l1[0]
        fl.append(calu*l2[0])
        fl2 += [l2[0]]
        return join_multiply(l1, l2[1:],fl,fl2)
    else:
        if len(l1) > 0:
            calu = l1[0]
            l1 = l1[1:]
            l2 = fl2
            return join_multiply(l1,l2,fl,[])
        else:
            return fl
            
result = []
join_multiply([4, 5], [3, 6, 8], result)
print(result)

result = []
join_multiply(list(range(10)), [5], result)
print(result)