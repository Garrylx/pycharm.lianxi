"""
@Project: pycharm.lianxi
@File: 旅行计划.py
@Author = GARKAX
@Date: 2022/9/13 17:28
TIME FLIES!
"""
# 70

n, m, k = map(int, input().split())
lst = []*(n+1)
q_lst = []*(m+1)
for i in range(n):
    t, c = map(int, input().split())
    lst.append([t, c])
target = 0
final_lst = (m+1)*[]
for j in range(m):
    final_t = int(input()) + k
    for i in lst:
        if i[0] >= final_t and i[1]-1 >= (i[0] - final_t):
            target += 1
    final_lst.append(target)
    target = 0
for x in final_lst:
    print(x)

# 100
# 差分数组，利用已知的核酸间隔时间，预计进入时间和要求间隔时间q+k <= t <= q+k+c-1
# 推出 t-c-k+1 <= q <= t-k 表示只要之后输入的k位于这个区间即可进入，因此应把timeline[t-c-k+1, t-k]
# 中的数组位置的值都加1表示符合标注，区间加法用到差分数组,注意timeline的下标都应大于0
n, m, k = map(int, input().split())
S = 200010
timeline = [0]*S
for i in range(n):
    t, c = map(int, input().split())
    time_p0 = max(t-c-k+1, 0)
    time_p1 = max(t-k, 0)
    # 标记区间  O(1)
    timeline[time_p0] += 1
    timeline[time_p1+1] -= 1
# 恢复原数组
for i in range(1, S):
    timeline[i] += timeline[i-1]

for k in range(m):
    q = int(input())
    print(timeline[q])






