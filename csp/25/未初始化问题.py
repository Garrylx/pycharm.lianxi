"""Author = GARKAX GY
Date: 2022--12
TIME FLIES!
"""
# 集合  需要单独判断yi等于0的情况
numOfVar, numOfSen = map(int, input().split())
set1 = set()
target = 0
for i in range(numOfSen):
    tmp1, tmp2 = map(int, input().split())
    if tmp2 not in set1 and tmp2 != 0:
        target += 1
    set1.add(tmp1)
print(target)

# 列表
n, k = map(int,input().split())
lst = [0]*(n+1)
target = 0
lst[0] = 1
for i in range(k):
    xi, yi = map(int,input().split())
    if lst[yi] == 0:
        target += 1
    lst[yi] = 1
print(target)


