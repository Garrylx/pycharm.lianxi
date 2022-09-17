"""author = "GARRY GY"
Date:2021-01-24

"""
#位置参数和关键字参数

#（aaa,end=""）end为关键字参数

print("a","A","v",sep="?",end="")
#sep关键字可以用“”内的分割输出的部分

def s(a,b=1,c=4):
    print(a)

s(2,c=5)#通过关键字参数修改某一个参数的默认值


def aa(*n):
    print(n)
#可以接受多个不同的n作为参数  并形成一个元组