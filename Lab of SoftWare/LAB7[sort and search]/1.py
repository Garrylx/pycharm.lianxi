"""author = "GARRY GY"
Date:2021-10-19
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""


def bubble_row(li,index):
    k = 0
    for i in range(len(li)-1): # 第i趟,每一躺会有一个最大的数变成有序的
        for j in range(len(li)-i-1): # 无序列表长度的索引
            if index > 0:
                if li[j+1] < li[j]:
                    li[j],li[j+1] = li[j+1],li[j]
                index -= 1
            else:
                break
        if index <= 0:
            break
    return  li

print(bubble_row(['m', 'v', 'o', 'd', 'h', 'l', 'y', 's', 'x', 'z'],4))