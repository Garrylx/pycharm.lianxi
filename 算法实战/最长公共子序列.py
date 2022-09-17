"""Author = GARKAX GY
Date: 2022--19
TIME FLIES!
"""
from typing import List


# 注解输入类型

# find length of the longest common subsequence of two sequences x and y
# m is the length of sequence x
# n is the length of sequence y
# c stores optimal values of subproblems
# rec is used to record computing information

# c[i][j]为在检查到str1[:i]和str2[:j]时最长子序列的长度
# rec 记录最后找到最大子序列长度后，如何找到最长子序列的路径【标记为LU的节点】【除了LU之外L为向左移动，U为向上移动】
# 在标记为LU的节点，最长子序列的末尾都增加了一个值
def LCSLength(x: str, y: str, m: int, n: int, c: List[List[int]], rec: List[List[int]]):
    # 初始化[第一行第一列为0]
    for i in range(m + 1):
        # 第0行的值为0
        c[i][0] = 0
    for j in range(1, n + 1):
        # 第0列的值为0，从1开始因为【0,0】已经为0
        c[0][j] = 0

    # 逐个遍历
    # 1-m
    for i in range(1, m + 1):
        # 1-n
        for j in range(1, n + 1):
            # 递推表达式
            if x[i-1] == y[j-1]:
                c[i][j] = c[i - 1][j - 1] + 1
                rec[i-1][j-1] = "LU"
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    # 如果在最长子序列长度数组中，左边的值比上边的值大，返回时往上走
                    c[i][j] = c[i - 1][j]
                    rec[i-1][j-1] = 'U'
                else:
                    # 如果在最长子序列长度数组中，上边的值比左边的值大，返回时往左走
                    c[i][j] = c[i][j - 1]
                    rec[i-1][j-1] = 'L'
    return c, rec


# construct optimal solution
# rec is used to record computing information
# x 为两者中较长序列用于输出最长序列
def PrintLCS(rec: List[List[int]], x: str, i: int, j: int):
    if i == 0 or j == 0:
        if rec[i][j] == "LU":
            print(x[i], end="")
        return
    if rec[i][j] == "LU":
        PrintLCS(rec, x, i - 1, j - 1)
        print(x[i], end="")
    elif rec[i][j] == "U":
        PrintLCS(rec, x, i-1, j)
    else:
        PrintLCS(rec, x, i, j-1)


# print length of the longest common subsequence
# print the longest common subsequence
def LCS(x: str, y: str):
    rec = [[str] * (100) for _ in range(100)] #  100x100数组
    c = [[int] * (100) for _ in range(100)]
    m = len(x)
    n = len(y)
    c, rec = LCSLength(x, y, m, n, c, rec)
    print(c[m][n])
    PrintLCS(rec, y, m-1, n-1)

x = 'ABCA'
y = 'BDCA'
LCS(x,y)