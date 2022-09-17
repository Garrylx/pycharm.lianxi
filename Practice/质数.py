oist = []
a = int(input())
for i in range(2,a+1):
    for j in range(2,a):
        if i%j == 0:
            break
    if i == j:
        oist.append(i)
print(oist)