"""Author = GARKAX GY
Date: 2022--19
TIME FLIES!
"""


# 参数解析 ： w : 未遍历过 g: 遍历过还没有变黑 b: 没有白色或灰色邻接节点 ,time 为时间戳参数

def dfs(adj_matrix):
    length = len(adj_matrix)
    # 栈，用于进行深度优先搜索，先入后出，直到回溯到根节点
    stack = []
    # 着色列表【标记灰白黑三种状态】
    colour = [""] * length
    # 父节点
    pre_node = [None] * length
    # 开始的时间戳
    seen = [0] * length
    # 结束的时间戳
    done = [0] * length
    # 初始化节点状态和父节点列表
    for i in range(length):
        colour[i] = 'w'
        pre_node[i] = None
    # 时间戳
    time = 0
    # 遍历图里面每一个白色定点【可能出现遍历森林】
    for node in range(length):
        if colour[node] == 'w':
            time = dfs_visit(node, colour, pre_node, seen, done, stack, time, adj_matrix)

    # tree_arc 遍历祖先数组，找每个索引对应的边
    tree_arc = []
    for x in range(length):
        if pre_node[x] is not None:
            tree_arc.append((pre_node[x], x))
    # 保证正序，可有可无
    tree_arc = sorted(tree_arc)

    # forward_arc back_arc cross arc
    forward_arc = []
    back_arc = []
    cross_arc = []
    for x in range(length):
        for y in range(length):
            dx = done[x]
            dy = done[y]
            sx = seen[x]
            sy = seen[y]
            # 保证两者是邻接节点
            if adj_matrix[x][y] == 1:
                #  不同边的条件表达式
                if dx > dy > sy > sx and (x, y) not in tree_arc:
                    forward_arc.append((x, y))
                if dy > dx > sx > sy:
                    back_arc.append((x, y))
                if dx > sx > dy > sy:
                    cross_arc.append((x, y))

    return tree_arc, forward_arc, back_arc, cross_arc


def dfs_visit(s, colour_lst, pre_list, seen_lst, done_lst, stack, time, adj_matrix):
    colour_lst[s] = 'g'
    seen_lst[s] = time
    #  每一次遍历时间戳+1
    time += 1
    # push入栈
    stack.insert(0, s)
    length = len(adj_matrix)
    while stack:
        # 操作栈顶的第一个元素
        cur = stack[0]
        # 判断是否有白色的邻接节点
        have_node = False
        for i in range(length):
            if adj_matrix[cur][i] == 1 and colour_lst[i] == 'w':
                colour_lst[i] = 'g'
                pre_list[i] = cur
                seen_lst[i] = time
                time += 1
                stack.insert(0, i)
                have_node = True
                break
        if not have_node:
            stack.pop(0)
            colour_lst[cur] = 'b'
            done_lst[cur] = time
            time += 1
    # 返回时间戳，确保时间是相连的
    return time


# adj_matrix = [[0, 0, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0],
#               [0, 1, 1, 1, 0, 0]]
# tree, forward, back, cross = dfs(adj_matrix)
# print('Tree arcs: {}'.format(tree))
# print('Forward arcs: {}'.format(forward))
# print('Back arcs: {}'.format(back))
# print('Cross arcs: {}'.format(cross))
# matrix = [[0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
# tree, forward, back, cross = dfs(matrix)
# print('Tree arcs: {}'.format(tree))
# print('Forward arcs: {}'.format(forward))
# print('Back arcs: {}'.format(back))
# print('Cross arcs: {}'.format(cross))


# adj_matrix = [[0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [1, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0]]
# tree, forward, back, cross = dfs(adj_matrix)
# print('Tree arcs: {}'.format(tree))
# print('Forward arcs: {}'.format(forward))
# print('Back arcs: {}'.format(back))
# print('Cross arcs: {}'.format(cross))
#
# """
# Tree arcs: [(0, 2), (1, 4), (2, 1), (4, 3)]↩
# Forward arcs: [(2, 3)]↩
# Back arcs: [(1, 0), (2, 0), (4, 2)]↩
# Cross arcs: []
# """

# adj_matrix = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
# tree, forward, back, cross = dfs(adj_matrix)
# print('Tree arcs: {}'.format(tree))
# print('Forward arcs: {}'.format(forward))
# print('Back arcs: {}'.format(back))
# print('Cross arcs: {}'.format(cross))

# ----------------------- Path judge----------------------

def is_reachable(adj_matrix, s, d):
    tree_arc, forward_arc, back_arc, cross_arc = dfs(adj_matrix)
    all_arcs = tree_arc + forward_arc + back_arc + cross_arc
    start_node = []
    end_node = []
    for i in range(len(all_arcs)):
        if all_arcs[i][0] not in start_node:
            start_node.append(all_arcs[i][0])
            end_node.append([all_arcs[i][1]])
        else:
            # 如果有出现相同开头的元素，就把结束点加到对应索引的结束列表的位置
            ind = start_node.index(all_arcs[i][0])
            end_node[ind] = end_node[ind] + [all_arcs[i][1]]
    # 倒着找
    stack = []
    signal = start_node.index(s)
    path = True
    pre = [signal]
    # 初始化
    if len(end_node[signal]) == 1:
        tmp = search(start_node, end_node[signal][0])
        if not tmp:
            return False
        else:
            signal = search(start_node, tmp)
            pre.append(tmp)
    else:
        stack = end_node[signal] + stack
        tmp = search(start_node,stack.pop(0))
        while not tmp:
            tmp = search(start_node, stack.pop(0))
        else:
            signal = search(start_node, tmp)
            pre.append(tmp)

# 修改signal
    while signal != d and path:
        if len(end_node[signal]) == 1:
            signal = search(start_node, end_node[signal][0])
            if signal in pre:
                pre = pre[:pre.index(signal)]
                if not pre:
                    pre = [s]
                if stack:
                    signal = stack.pop()
                else:
                    path = False
            else:
                pre.append(signal)
            if signal > len(start_node) - 1:
                while signal > len(start_node) - 1 and stack:
                    signal = stack.pop(0)
                else:
                    if not stack:
                        path = False
                    else:
                        signal = stack.pop(0)
            else:
                continue
        else:
            stack = end_node[signal] + stack
            tmp = stack.pop(0)
            signal = search(start_node, tmp)
            pre.append(tmp)
            if signal in pre:
                pre = pre[:pre.index(signal)]
                if not pre:
                    pre = [s]
                if stack:
                    signal = stack.pop()
                else:
                    path = False
            else:
                pre.append(signal)
            if signal > len(start_node) - 1:
                while signal > len(start_node) - 1 and stack:
                    signal = stack.pop(0)
                else:
                    if not stack:
                        path = False
                    else:
                        signal = stack.pop(0)
            else:
                continue
    return path


def search(start_node, ind):
    if ind in start_node:
        return start_node.index(ind)
    else:
        return False


adj_matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0]
]
print(is_reachable(adj_matrix, 4, 4))
print(is_reachable(adj_matrix, 0, 2))
