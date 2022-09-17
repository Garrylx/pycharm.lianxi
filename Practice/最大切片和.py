"""author = "GARRY GY"
Date:2021-07-09
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
# 最大切片和
# 从第一个值往后相加求和，每次减小一个长度，操作完以后移除第一个值。重复前面的操作
alist = input()
alist = alist.split()
alist = list(map(int,alist))
lens = len(alist)
blist = []
clist = []
for j in range(lens): # 循环原列表长度次
    for i in alist:# 产生一个新blist
        blist.append(i)
    while len(blist) > 0: # 直到blist清空
        clist.append(sum(blist))
        blist = blist[:-1]
    alist.remove(alist[0]) #移除列表的第一个值
print(max(clist))#把和列表中的最大值输出