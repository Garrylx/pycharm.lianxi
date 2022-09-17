"""author = "GARRY GY"
Date:2020-12-17

"""
lista = []
a = int(input())
while a != -1:
    lista.append(a)
    a = int(input())
print(lista)

k = 0
listyuanzu = []
set1 = set(lista)
print(set1)
for j in set1:
    for i in lista:
        if i == j:
            k +=1
        else:
            continue
    yuanzu = (j,k)
    listyuanzu.append(yuanzu)
    k = 0
for item in listyuanzu:
    print(item)