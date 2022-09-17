import time
s = time.perf_counter()

n, l, s = map(int, input().split())
points = [[i for i in map(int,input().split())] for j in range(n)]
temp = {}
for point in points:
    x, y = point[0], point[1]
    temp[(x, y)] = 1
money = []
for i in range(s+1):
    money.insert(0, list(map(int, input().split())))
t = 0
for x, y in points:
    flag = 0
    for i in range(s+1):
        for j in range(s+1):
            if (x+i > l) or (y+j > l):
                flag = 1
                break
            if money[i][j]:
                if (x+i, y+j) not in temp:
                    flag = 1
                    break
            else:
                if (x+i, y+j) in temp:
                    flag = 1
                    break
        if flag == 1:
            break
    if flag == 0:
        t += 1
print(t)
e = time.perf_counter()
print(e-s)
