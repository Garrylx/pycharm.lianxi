"""author = "GARRY GY"
Date:2021-04-19

"""

def YHSJ_gen():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]
n = int(input())
m = 0
for res in YHSJ_gen():
    while n > m:
        print(res)
        m += 1
        break
#