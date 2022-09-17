"""author = "GARRY GY"
Date:2021-01-24

"""
#在同一文件夹内导入模块
import apple as t

print(t.apple())
#方式一

from apple import apple as new_apple

print(new_apple())
#方式二


from apple import *
#导入模块中所有函数

