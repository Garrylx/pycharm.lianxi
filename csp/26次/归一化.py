"""Author = GARKAX GY
Date: 2022--11
TIME FLIES!
"""
import math

n = int(input())
str1 = input()
tmp_list = str1.split()
n_list = [int(x) for x in tmp_list]


x = sum(n_list) / n
tmp_list = []
for i in n_list:
    tmp = math.pow(x - i, 2)
    tmp_list.append(tmp)
D_a = sum(tmp_list) / n
f_a = [(i - x)/math.sqrt(D_a) for i in n_list]
for x in f_a:
    print(x)