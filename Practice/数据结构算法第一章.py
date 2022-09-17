"""author = "GARRY GY"
Date:2021-04-25

"""
# # 1
# def is_multiple(n,m):
#     s = n%m
#     if s == 0 :
#         return True
#     else:
#         return  False
# n = int(input())
# m = int(input())
#
# print(is_multiple(n,m))

# # 2
# def is_even(k):
#     return True if k & 1 == 0 else False
#
# k = int(input())
# print(is_even(k))

# #3
# def minmax(lists=[]):
#     lists = sorted(lists)
#     return lists[0],lists[-1]
#
#
# num = int(input())
# data = []
#
# for i in range(num):
#     a= int(input())
#     data.append(a)
# print(minmax(data))

# # 4
# def f(n):
#     lists = []
#     for i in range(1,n+1):
#         lists.append(i**2)
#     return sum(lists)

# # 5
# def sum_s(n):
#     lists = [i**2 for i in range(1,n+1)]
#     return sum(lists)

# # 6
# def yo(n):
#     lists = []
#     for i in range(1,n+1):
#         if i%2 == 0:
#             pass
#         else:
#             lists.append(i**2)
#     return sum(lists)


# # 7
# def yos(n):
#     lists = [i**2 for i in range(1,n+1) if i%2 != 0]
#     return sum(lists)

##8
# lists = []
# j = len(lists)+ k

## 9
# for i in range(50,81,10):
#     print(i)

## 10
# for i in range(-8,9,2):
#     print(i)

##11
# k = 2
# lists = [k**i for i in range(8)]
# print(lists)

##12
#
# def choice(n,m):
#     import random
#     return random.randrange(n,m+1)

## 13
# lists = []
# print(lists[::-1])

## 14
# lists = []
# listss = list(set(lists))
# for i in listss:
#     if i % 2 == 0:
#         listss.remove(i)
#
# if len(listss) != 0:
#     print("True")
# else:
#     print("False")

## 15
# a = []
# b = set(a)
# if len(b) == len(a):
#     print("T")
# else:
#     print("F")

## 16
# 通过data[j]把data中索引为j元素读出来，乘上一个fact 并把这个值再赋给data【j】

## 17
#不行，因为这样只是调用了列表中的值，而没有对应列表中元素的地址

##18
# k = 0
# 等差lists = [i*(I+1) for i in range(1,10)]

## 19
# lists = [chr(ord("a")+x) for x in range(26)]
# print(lists)


## 20


## 21
# def python_pop():
#     a = []
#     while 1:
#         try:
#             b = input()
#             a.append(b)
#         except KeyboardInterrupt:
#             while len(a) != 0:
#                 a.pop()
# python_pop()

## 22
# def x(a,b):
#     c = []
#     for i in len(a):
#         y = a[i]*b[i]
#         c.append(y)
#
# # a,b为数组

## 23
# def Yuejie(lists,i):
#     try:
#         return lists[i]
#     except IndexError:
#         print("Don't try buffer overflow attracks in python!")


# # 24
# def jisuan(lists):
#     p = 0
#     x = ["a","i","e","o","u"]
#     for i in range(len(lists)):
#         if lists[i] in x:
#             p += 1
#         else:
#             pass
#
#     return p


## 25

#
# string = input()
# st = string.replace(".","")
# st1 = st.replace(",","")
# st2 = st1.replace(("'",""))
# print(st2)

## 26
# def hanshu():
#     a = input()
#     a = list(a.split())
#     a1 = int(a[0])
#     a2 = int(a[1])
#     a3 = int(a[2])
#     if a1 + a2 == a3 or a2 - a3 == a1 or a1 * a2 == a3:
#         return  True
#     else:
#         return False

## 27
# def dx(n):
#     k = 1
#     te = []
#     while k*k < n:
#         if n % k == 0:
#             yield k
#             te.append(n//k)
#         k += 1
#     if k*k == n:
#         yield k
#     else:
#         pass
#     for i in te[::-1]:
#         yield  i
# n = input()
# print(dx(n))

## 28
# def x(v,p):
#     import math
#     return math.sqrt(sum(pow(i,p) for i in v))



# # 29
# def remove_str():
#     import random
#     lists = ["c","a","t","d","o","g"]
#     listss = []
#     str_lists = []
#     for i in range(21):
#         for i in range(6):
#             x = random.choice(lists)
#             listss.append(x)
#             lists.remove(x)
#         for item in listss:
#             k = ""
#             k += item
#         str_lists.append(k)
#         print(k)
#
# def x_dw():
#     lists = ["c", "a", "t", "d", "o", "g"]
#     from itertools import permutations as pe
#     print(list(pe(lists)))
# 新 iteration tools


# # 30
# n = int(input())
# x = 0
# while n > 2:
#     n = n//2
#     x += 1
# print(x)

# # 31

# def charge_100(gut):
#     a = gut%100
#     b = gut//100
#     if a == 0:
#         print("支付0张100")
#         return gut
#     else:
#         print("支付{}张100".format(b))
#         gut = gut-b*100
#         return gut
#
# def charge_50(gut):
#     a = gut%50
#     b = gut//50
#     if a == 0:
#         print("支付0张50")
#         return gut
#     else:
#         print("支付{}张50".format(b))
#         gut = gut - b*50
#         return gut
#
# def charge_20(gut):
#     a = gut % 20
#     b = gut//20
#     if a == 0:
#         print("支付0张20")
#         return gut
#     else:
#         print("支付{}张20".format(b))
#         gut = gut - b * 20
#         return gut
#
# def charge_10(gut):
#     a = gut % 10
#     b = gut//10
#     if a == 0:
#         print("支付0张10")
#         return gut
#     else:
#         print("支付{}张10".format(b))
#         gut = gut - b * 10
#         return gut
#
# def charge_5(gut):
#     a = gut % 5
#     b = gut//5
#     if a == 0:
#         print("支付0张5")
#         return gut
#     else:
#         print("支付{}张5".format(b))
#         gut = gut - b * 5
#         return gut
#
# def charge_1(gut):
#     return print("支付{}张1".format(gut))
#
#
#
# def charge(gut):
#     charge_1(charge_5(charge_10(charge_20(charge_50(charge_100(gut))))))
#
# pay = int(input())
# price = int(input())
# gut = pay - price
# if gut == 0:
#     pass
# else:
#     charge(gut)



##  31 & 32
# def calculate(str_o):
#     n1 = int(str_o[0])
#     n2 = int(str_o[2])
#
#     if "+" in str_o:
#         return n1 + n2
#     elif "-" in str_o:
#         return n1 - n2
#     elif "*" in str_o:
#         return n1 * n2
#     elif "/" in str_o:
#         return  n1/n2
#
#
# while True:
#     try:
#         str_operate = input("输入以空格分割的操作语句")
#
#         if "clear" in str_operate:
#             print("清除")
#             str_operate = ""
#             continue
#         elif str_operate == "break":
#             print("计算器关闭")
#             break
#         elif "+"in str_operate or "-"in str_operate or "*" in str_operate or "/" in str_operate and "clear" not in str_operate:
#             str_o = str_operate.split()
#             print(calculate(str_o))
#         else:
#             raise (ValueError)
#     except ValueError as x:
#         print("输入错误",x)
#

## 34
# def punishment():
#     str1 = "I will never spam my friends"
#     k = 0
#     j = 0
#     while k < 8 and j < 100:
#         str2 = input("请输入惩罚句式")
#         if str2 == str1:
#             j += 1
#             pass
#         else:
#             j += 1
#             k += 1
#     if k >= 8:
#         print("错误过多")
#     else:
#         print("惩罚结束")
#
#
# punishment()


## 35

# def birthday(num):
#     import math
#     p = 1 - math.pow((364/365), (num*(num-1)/2))
#     return p
# num = int(input())
# print(birthday(num))


# # 36
# a = input()
# b = a.split()
# c = set(b)
# def collect_str(item,b):
#     j = 0
#     for i in b:
#         if i == item:
#             j += 1
#         else:
#             pass
#     print("一共{}个".format(j) + str(item))
#
# for item in c:
#     collect_str(item,b)






















