"""author = "GARRY GY"
Date:2021-07-21
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
# 像摸牌一样，摸一张插进去
def insert_sort(lis):
    for i in range(1,len(lis)):
        tmp = lis[i]
        j = i-1 #取摸得牌左边的有序区第一个开始比较
        while j >= 0 and lis[j] > tmp:#在没有移到最左端之前，如果手上的当前数字大于抽出来的数字
            lis[j+1] = lis[j]# 把这个数字往右移动一个
            j -= 1#索引往左一位
        lis[j+1] = tmp# 当有序的牌不大于抽出的牌或者手里的数字到头时，把牌放在当前牌的上一个
        print(lis)
# 时间复杂度为n**2

lis = ['x', 'b', 'f', 'u', 'r', 'k']
insert_sort(lis)