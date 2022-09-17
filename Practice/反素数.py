num = input()
listnum1 = []
for letter in num:
    listnum1.append(letter)
listnum2 = listnum1[::-1]

n1 = int(num)
n2 = int("".join(listnum2))

def judge(n):
    for i in range(2,n):
        if n % i == 0:
            break

        else:
            if i == n-1:
                return n
if judge(n1) == judge(n2):
    print("No")
else:
    print(judge(n1),judge(n2),end="")

