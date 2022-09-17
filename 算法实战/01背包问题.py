from typing import List

"""Author = GARKAX GY
Date: 2022--19
TIME FLIES!
"""

# find the maximum value of knapsack
"""

n is the number of items 【物品数量】
C is the maximum capacity of knapsack 【表示背包容量】
v lists values of the items, the ith item is worth vi 【记录物品的价值，第i个】
w lists weight of the items, the ith item weighs wi 【记录物体的重量，第i个】
m stores the optimal values of sub_problems 最优子问题
rec is used to record computing information 记录计算值【如何返回】

"""
# ----------------参数解析---------------------------------

#  m[i, j] 代表假设背包容量为j，且可选择物品位于第0到第i个之间时，背包可以装的 最大价值
#  状态转移方程 m[i,j] = Max{ m[i-1,j-Wi]+Vi( j >= Wi ),  m[i-1,j] }
# rec中参数： up = 0 jump = 1

# ------------状态转移方程参数解析-----------------------------
"""
m[i-1,j-Wi]+Vi( j >= Wi ) j-w代表背包在没有放第i物体时的容量，i-1代表第i个物体不位于选择范围内时的选择范围
                           vi代表i的价值【j>=w】因为当包容量小于当前第i个物品的重量时，一个也装不进去
"""

"""
m[i-1, j] 代表如果不装第i个物体，当物体选择范围在第0-i-1个，背包容量为j时的可装的最大价值
"""


# 获得最大的背包价值
def find_optimal_value(n: int, c: int, v: List[int], w: List[int], m: List[List[int]], rec: List[List[int]]):
    # 由于传入的参数格式问题把第0行第0列初始化为0
    for i in range(1, n + 1):
        m[i][0] = 0
    for j in range(c + 1):
        m[0][j] = 0
        rec[0][j] = 0
        # 初始化当只放第一个物体时的二维数组
        # 第一个物体都放不下时最大价值为0，rec标记为0，表示没有取
        if j < w[1]:
            m[1][j] = 0
            rec[1][j] = 0
        #  能放下第一个物体时最大价值为第一个物体的价值，rec 标记为1表示取了
        else:
            m[1][j] = v[1]
            rec[1][j] = 1

    # 逐个遍历【递推表达式】
    # 外层循环为第2个到第n物体[第1个已经初始化过了]
    for item in range(2, n + 1):
        # 内层循环为背包当前容量从0到m
        for cur_bag_weight in range(c + 1):
            var_without_i = m[item - 1][cur_bag_weight]
            if cur_bag_weight - w[item] >= 0:
                var_put_i = m[item - 1][cur_bag_weight - w[item]] + v[item]
            else:
                var_put_i = 0
            # 如果不放入物体i时的最大价值大，那么包含第i个物体时应不放入第i个
            # 如果没有放入物体i，那么返回时应该向上走【0-i-1个物体】
            if var_without_i >= var_put_i:
                m[item][cur_bag_weight] = var_without_i
                # 从第二个物品开始的记录
                rec[item][cur_bag_weight] = 0
            # 放入第i个物体说明这个物体就是我们的最优解的组成部分
            else:
                m[item][cur_bag_weight] = var_put_i
                rec[item][cur_bag_weight] = 1
    return m, rec


# 形成最优结果
# construct the optimal solution
def find_optimal_solution(rec: List[List[int]], n: int, c: int, w: List[int], x=None):
    if x is None:
        x = []
    if n == 0 or c == 0:
        x.insert(0, 0)
        return
    if rec[n][c] == 0:
        x.insert(0, 0)
        find_optimal_solution(rec, n - 1, c, w, x)
    else:
        x.insert(0, 1)
        tmp = c - w[n]
        find_optimal_solution(rec, n - 1, tmp, w, x)
    if len(x) == n + 1:
        print(x)


# print the optimal value and optimal solution
# 主函数
def knapsack(c: int, n: int, v: List[int], w: List[int]):
    rec = [[int] * (100) for _ in range(100)]
    m = [[int] * (100) for _ in range(100)]
    m, rec = find_optimal_value(n, c, v, w, m, rec)
    print(m[n][c])
    find_optimal_solution(rec, n, c, w)
    return 0


# o_C = 16
# o_n = 3
# o_v = [-1, 5, 4, 1]
# o_w = [-1, 10, 8, 5]
# knapsack(o_C, o_n, o_v, o_w)
