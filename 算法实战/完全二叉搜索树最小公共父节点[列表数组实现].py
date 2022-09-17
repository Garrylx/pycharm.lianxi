"""Author = GARKAX GY
Date: 2022--18
TIME FLIES!
"""
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)

    def insert_left(self, data):
        self.left = data

    def insert_right(self, data):
        self.right = data


class BST:
    def __init__(self, root=None):
        self.root = []

    def insert(self, key):
        a = Node(key)
        self.root.append(a)
        i1 = self.root.index(a)
        ir = (i1 - 1) // 2
        if i1 % 2 == 0:
            self.root[ir].right = self.root[i1]
        else:
            self.root[ir].left = self.root[i1]

    def search(self, key):
        index_lst = [x.data for x in self.root]
        for x in index_lst:
            if key == x:
                ind = index_lst.index(x)
                return self.root[ind]
        else:
            return None


def lca(in_bst, x, y):
    index_lst = [x.data for x in in_bst.root]
    lx = []
    if x in index_lst and y in index_lst:
        i_x = index_lst.index(x)
        i_y = index_lst.index(y)
        while i_x != 0:
            i_x = (i_x - 1) // 2
            lx.append(i_x)
        while i_y != 0:
            i_y = (i_y - 1) // 2
            if i_y in lx:
                return index_lst[i_y]
    else:
        return None


def to_bst(lst):
    # print(id(keys))
    # keys = sorted(keys) 这次赋值会改变keys的地址，只能直接sorted()
    n = len(lst)
    tmp = sorted(lst)
    # 不会改变keys地址的赋值，并对tmp进行 操作
    # print(id(tmp))
    # print(id(keys)) 地址不同
    tmp = [x for x in mid_walk(tmp, 0, n, [])]
    for x in range(n):
        lst[x] = tmp.pop(0)


def mid_walk(lst, node, length, tmp):
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


keys = [10, 8, 13, 7, 9, 11, 15]
bst = BST()
for key in keys:
    bst.insert(key)
print(lca(bst, 7, 9))

keys = [72, 78, 90, 94, 81, 43, 49, 60, 50, 91]
to_bst(keys)
bst = BST()
for key in keys:
    bst.insert(key)
print(lca(bst, 91, 81))

keys = [91, 82, 21, 4, 23, 73, 69, 82, 71, 97]
to_bst(keys)
bst = BST()
for key in keys:
    bst.insert(key)
print(lca(bst, 4, 80))

# self.root = Node(None)
#         length = len(key)
#         key[0] = Node(key[0])
#         key[1] = Node(key[1])
#         self.root.insert_left(key[0])
#         self.root.insert_right(key[1])
#         r_g = (length-1)//2 if length%2 == 0 else (length-2)//2
#         for x in range(r_g):
#             l = 2 * x + 1
#             r = l + 1
#             if l < length:
#                 key[l] = Node(key[l])
#                 key[x].insert_left(key[l])
#             if r < length:
#                 key[r] = Node(key[r])
#                 key[x].insert_right(key[r])
#         return key
