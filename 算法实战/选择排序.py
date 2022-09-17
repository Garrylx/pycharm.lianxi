"""author = "GARRY GY"
Date:2021-07-21
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

# 选择出最小的一个
def select_sort(li):
    lis = []
    for i in range(len(li)):
        min_val = min(li) #o(n)
        lis.append(min_val)
        li.remove(min_val)#o(n)
    return li

# 算法生成了两个列表 占用内存大
# remove在移除后不能产生空位，需要往前补，空间复杂度增加

def my_selection_sort(data):
    for i in range(len(data) - 1):
        min_1 = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_1]:
                min_1 = j
        data[i],data[min_1] = data[min_1],data[i]
    return data