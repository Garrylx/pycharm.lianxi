"""author = "GARRY GY"
Date:2021-07-13
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

# 也叫线性查找，从列表第一个元素开始，顺序进行搜索，直到找到元素或者到最后一个元素为止

def linear_search(lis,value):
    for i, v in enumerate(lis):  # 用enumerate更加快捷
        if v == value:
            return i
        else:
            return None

