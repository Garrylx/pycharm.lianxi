"""author = "GARRY GY"
Date:2020-12-03

"""
#浮点数计算不精确
#导入Decimal 进行精确运算
a = 1.1
b = 2.2
print(a+b)

from decimal import Decimal
a = 1.1
b = 2.2
print(Decimal("1.1")+Decimal("2.2"))

a = True
b = False
print(1+a)#True的值为1 false的值为0
print(1+b)
