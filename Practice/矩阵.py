import numpy as np
lists = []
n = int(input())
for i in range(n**2):
    n = int(input())
    lists.append(n)
m2 = np.array(lists).reshape(n,n)
print(m2)