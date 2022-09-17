"""author = "GARRY GY"
Date:2021-12-14
"""


class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, left=self.__left)
            self.__left = tree

    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinaryTree(new_data)
        else:
            tree = BinaryTree(new_data, right=self.__right)
            self.__right = tree

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right


def sum_leaves(my_tree):
    if my_tree is not None:
        if my_tree.get_left() is not None or my_tree.get_right() is not None:
            return sum_leaves(my_tree.get_left()) + sum_leaves(my_tree.get_right())
        else:
            return my_tree.get_data()
    else:
        return 0


class Queue(object):
    def __init__(self):
        self.__items = []

    def is_empty(self):
        if self.__items is []:
            return True

    def enqueue(self, item):
        self.__items.insert(0, item)

    def dequeue(self):
        if self.__items != []:
            return self.__items.pop()
        else:
            raise IndexError

    def get_items(self):
        return self.__items

    def size(self):
        return len(self.__items)

    def peek(self):
        if self.__items == []:
            raise IndexError
        else:
            return self.__items[len(self.__items) - 1]

    def __str__(self):
        return "Queue: {}".format(self.__items)

    def __len__(self):
        return len(self.__items)


def breadth_traversal(my_tree):
    node_list = []
    q = [my_tree]
    while q != []:
        node_list.append(q[0].get_data())
        if q[0].get_left() is not None:
            q.append(q[0].get_left())
        if q[0].get_right() is not None:
            q.append(q[0].get_right())
        q.pop(0)

    return node_list


t1 = BinaryTree(5)
t1.insert_left(2)
t1.insert_left(3)
t1.insert_right(1)
t1.insert_right(4)
print(breadth_traversal(t1))
