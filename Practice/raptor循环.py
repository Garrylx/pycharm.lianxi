"""author = "GARRY GY"
Date:2020-11-24

"""
"""def f(n):
    if n == 1:
        return n
    else:
        return n *f(n-1)
n = int(input())
print(f(n))"""

class AlwaysPositive:
    def __init__(self,number):
        self.n = number
    def __add__(self,other):
        return abs(self.n + other.n)

a = AlwaysPositive(-20)
b = AlwaysPositive(1)

print(a+b)