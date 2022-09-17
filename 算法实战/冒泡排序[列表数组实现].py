"""author = "GARRY GY"
Date:2021-07-21
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def bubble_sort(li):
    for i in range(len(li)-1): # 第i趟,每一躺会有一个最大的数变成有序的，最后一遍最后一个元素自动在最后个
        exchange = False # 改进，当某一趟中没有出现交换时
        for j in range(len(li)-i-1) : # 无序列表长度的索引
            if li[j+1] < li[j]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        if not exchange:
            return li

bubble_sort([54, 78, 18, 61, 13, 93])