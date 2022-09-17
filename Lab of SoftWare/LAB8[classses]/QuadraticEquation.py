"""author = "GARRY GY"
Date:2021-10-20
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
from  math import *
class QuadraticEquation(object):

    def __init__(self,coeff_a=1,coeff_b=1,coeff_c=1):
        self.__coeff_a = coeff_a
        self.__coeff_b = coeff_b
        self.__coeff_c = coeff_c

    def get_coeff_a(self):
        return self.__coeff_a

    def get_coeff_b(self):
        return self.__coeff_b

    def get_coeff_c(self):
        return self.__coeff_c

    def get_discriminant(self):
        b = self.__coeff_b
        a = self.__coeff_a
        c = self.__coeff_c

        res = b**2 - 4*a*c
        return res

    def has_solution(self,):
        if QuadraticEquation.get_discriminant(self) >= 0:
            return True
        else:
            return False

    def get_root1(self):
        a = self.__coeff_a
        b = self.__coeff_b
        c = self.__coeff_c
        root1 = (-b + sqrt(b**2 - 4*a*c))/ (2*a)
        return format(root1,".2f")

    def get_root2(self):
        a = self.__coeff_a
        b = self.__coeff_b
        c = self.__coeff_c
        root2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return format(root2,".2f")

    def __str__(self):
        if QuadraticEquation.get_discriminant(self) > 0:
            return "The roots are %s and %s." % (QuadraticEquation.get_root1(self),QuadraticEquation.get_root2(self))

        elif QuadraticEquation.get_discriminant(self) == 0:
            return "The root is %s." % (QuadraticEquation.get_root1(self))

        else:
            return "The equation has no roots."


equation1 = QuadraticEquation(4, 4, 1)
print(equation1.get_root1(), equation1.get_root2())
equation3 = QuadraticEquation(1, 2, -63)
print(equation3.get_root1(), equation3.get_root2())
