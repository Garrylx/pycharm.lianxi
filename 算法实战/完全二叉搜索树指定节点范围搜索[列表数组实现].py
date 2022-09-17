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


def range_search(self_bst, self_range):
    index_lst = [x.data for x in self_bst.root]
    tmp = []
    for x in index_lst:
        if range[0] <= x <= range[1]:
            tmp.append(x)
    return sorted(tmp)


keys = [10, 8, 13, 7, 9, 11, 14]

bst = BST()
for key in keys:
    bst.insert(key)

print(range_search(bst, [9, 13]))
