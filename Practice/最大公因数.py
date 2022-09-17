"""author = "GARRY GY"
Date:2020-12-17

"""

alist = []
def judge(a,b):
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    else:

        c = min(a,b)
        for j in range(2,c+1):
            for k in range(2,c):
                if j%k == 0:
                    break
            if j == k:
                alist.append(j)

        blist = []

        for i in range(2,c+1):
            if a%i == 0 and b%i == 0 and i in alist:
                blist.append(i)
        k = 1
        for num in range(len(blist)):
            k = blist[num] * k
        return k
a = int(input())
b = int(input())
print(judge(a,b))

