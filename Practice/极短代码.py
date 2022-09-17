"""author = "GARRY GY"
Date:2020-11-26

"""
#以下方法可以检查给定列表是不是存在重复元素，它会使用 set() 函数来移除所有重复元素。
"""def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # False
all_unique(y) # True"""



#检查两个字符串的组成元素是不是一样的。


"""from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)


anagram("abcd3", "3acdb") # True"""




#下面的代码块可以检查变量 variable 所占用的内存。
"""import sys 

variable = 30 
print(sys.getsizeof(variable)) # 24"""


#下面的代码块可以检查字符串占用的字节数。
"""def byte_size(string):
    return(len(string.encode('utf-8')))


byte_size(' ') # 4
byte_size('Hello World') # 11"""

#打印 N 次字符串,该代码块不需要循环语句就能打印 N 次字符串。
"""n = 2; 
s ="Programming"; 

print(s * n);
# ProgrammingProgramming"""


#大写第一个字母,以下代码块会使用 title() 方法，从而大写字符串中每一个单词的首字母。

"""s = "programming is awesome"

print(s.title())
# Programming Is Awesome"""

#分块
#给定具体的大小，定义一个函数以按照这个大小切割列表

'''from math import ceil

def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))



chunk([1,2,3,4,5],2)
# [[1,2],[3,4],5]'''


#压缩,这个方法可以将布尔型的值去掉，例如（False，None，0，“”），它使用 filter() 函数。

