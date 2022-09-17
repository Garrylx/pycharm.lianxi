"""Author = GARKAX GY
Date: 2022--11
TIME FLIES!
"""
# n, l, s = map(int, input.split())

str1 = input()
list_all = [int(x) for x in str1.split()]
tree_matrix = []
map_matrix = []
S = list_all[-1]
L = list_all[1]
for x in range(list_all[0]):
    tree = input()
    tree_matrix.append([int(x) for x in tree.split()])

for x in range(S+1):
    maps = input()
    map_matrix.insert(0, [int(x) for x in maps.split()])

map_point1 = []
map_point0 = []
for i in range(S+1):
    for j in range(S+1):
        if map_matrix[i][j] == 1:
            map_point1.append((i, j))
        else:
            map_point0.append((i, j))

match = True
target = 0

#40
for x in range(L+1):
    if target == list_all[0]:
        break
    for y in range(L+1):
        for ind in map_point1:
            xi = x + ind[0]
            yi = y+ind[1]
            if [xi, yi] not in tree_matrix or xi > L or yi > L:
                match = False
                break
            else:
                match = True
        if match:
            for ind in map_point0:
                xi = x + ind[0]
                yi = y + ind[1]
                if [xi, yi] in tree_matrix or xi > L or yi > L:
                    match = False
                    break
        if match:
            target += 1
        if target == list_all[0]:
            break
print(target)

# 60 注意左下角一定是一棵树
detected = []
for tr in tree_matrix:
    for p in map_point1:
        x0, y0 = tr[0]-p[0], tr[1]-p[1] # 找到初始点
        if x0 >= 0 and y0 >= 0 and [x0, y0] not in detected: # 在林子内
            detected.append([x0, y0])
            for pi in map_point1:
                xi, yi = x0+pi[0], y0+pi[1]
                if [xi, yi] not in tree_matrix or xi > L or yi > L:
                    match = False
                    break
                else:
                    match = True
            if match:
                for ind in map_point0:
                    xi, yi = x0 + ind[0], y0 + ind[1]
                    if [xi, yi] in tree_matrix or xi > L or yi > L:
                        match = False
                        break
            if match:
                target += 1
        else:
            continue

print(target)


# 100
n, l, s = map(int, input().split())
points = [[i for i in map(int, input().split())] for j in range(n)]
temp = {}
for point in points:
    x, y = point[0], point[1]
    temp[(x, y)] = 1
mmap = []
for i in range(s+1):
    mmap.insert(0, list(map(int, input().split())))
t = 0
for x, y in points:
    key = 0
    for i in range(s+1):
        for j in range(s+1):
            if (x+i > l) or (y+j > l):
                key = 1
                break
            if mmap[i][j]:
                if (x+i, y+j) not in temp:
                    key = 1
                    break
            else:
                if (x+i, y+j) in temp:
                    key = 1
                    break
        if key == 1:
            break
    if key == 0:
        t += 1
print(t)






