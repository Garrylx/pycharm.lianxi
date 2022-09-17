"""Author = GARKAX GY
Date: 2022--18
TIME FLIES!
"""


# 完全二叉搜索树：对有序序列进行中序遍历在形成树

def to_bst(keys):
    # print(id(keys))
    # keys = sorted(keys) 这次赋值会改变keys的地址，只能直接sorted()
    n = len(keys)
    tmp = sorted(keys)
    # 不会改变keys地址的赋值，并对tmp进行 操作
    # print(id(tmp))
    # print(id(keys)) 地址不同
    tmp = [x for x in mid_walk(tmp, 0, n, [])]
    for x in range(n):
        keys[x] = tmp.pop(0)


def mid_walk(lst, node, length, tmp=[]):
    left = node * 2 + 1
    right = left + 1
    if left < length:
        mid_walk(lst, left, length, tmp)
    else:
        tmp.append(lst[node])
    if right < length:
        tmp.append(lst[node])
        mid_walk(lst, right, length, tmp)
    else:
        # 当只有左子节点时
        if tmp[-1] != lst[node]:
            tmp.append(lst[node])
        return
    return tmp
