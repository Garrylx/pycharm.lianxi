"""author = "GARRY GY"
Date:2020-11-26

"""
n = int(input())
lists = []
relists = []
while n != -1:
    lists.append(n)
    n = int(input())
for i in range(len(lists)):
    relists.append(min(lists))
    lists.remove(min(lists))

list2 = list(set(relists))

for i in list2:
    num = relists.count(i)
    final = (i,num)
    print(final)