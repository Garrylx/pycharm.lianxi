"""author = "GARRY GY"
Date:2021-11-29
"""
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def insert_left(self, new_data):
        if self.__left == None:
            self.__left = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, left=self.__left)
            self.__left = t

    def insert_right(self, new_data):
        if self.__right == None:
            self.__right = BinarySearchTree(new_data)
        else:
            t = BinarySearchTree(new_data, right=self.__right)
            self.__right = t
    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
# 判断数据是否在整个二叉树中
    # 类中的递归
    def __contains__(self,item,data_list=[]):
        while self.__data is not None:
            data_list.append(self.__data)
            if self.__left is not None:
                self.__left.__contains__(item,data_list)
                # self._left如果不是None的话，则它本身也会是一个对象，在调用方法使默认会先传入参数self
            if self.__right is not None:
                self.__right.__contains__(item,data_list)
            break
        if item in data_list:
            return True
        else:
            return False

# tree = BinarySearchTree(15,BinarySearchTree(2),BinarySearchTree(3,BinarySearchTree(8),BinarySearchTree(10)))
# print(14 in tree)
# print(10 in tree)

# 判断是否存在某个值并返回这个节点

    def search(self, value,data_list={}):
        while self.__data is not None:
            data_list[self.__data] = self
            if self.__left is not None:
                self.__left.search(value,data_list)
            if self.__right is not None:
                self.__right.search(value,data_list)
            break
        if value in data_list.keys():
            return data_list[value]
        else:
            return None


    def insert(self, value):
        # while self.__data is not None:
            if value > self.__data:
                if self.__right is not None:
                    self.__right.insert(value)
                else:
                    self.insert_right(value)
            elif value < self.__data:
                if self.__left is not None:
                    self.__left.insert(value)
                else:
                    self.insert_left(value)
            elif value == self.__data:
                self.insert_left(value)

        # else:
        #     self.insert_left(value)

# t = BinarySearchTree(15,BinarySearchTree(2),BinarySearchTree(17,BinarySearchTree(16),BinarySearchTree(18)))
# tree.insert(17.5)
# print_tree(tree,0)

def create_bst_from_list(values):
    values = bubble_sort(values)
    index = (len(values)+1)//2
    head = BinarySearchTree(values[index])
    for i in values[1:]:
        if i != head:
            head.insert(i)
    return head

# recursion
def create_bst_from_sorted(values):
    if len(values) > 1:
        target = BinarySearchTree(values[len(values)//2])
        l_list = values[:len(values)//2]
        m_list = values[len(values)//2+1:]
        if len(l_list) > 1:
            target.set_left(create_bst_from_sorted(l_list))
        else:
            target.set_left(BinarySearchTree(l_list[0]))
        if len(m_list) > 1:
            target.set_right(create_bst_from_sorted(m_list))
        elif len(m_list) == 1:
            target.set_right(BinarySearchTree(m_list[0]))
        return target
    else:
        return BinarySearchTree(values[0])

def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data()))
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1)
    if tree.get_right() != None:
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)

#
# t = create_bst_from_sorted([1,3,5,7,9,11,13,15,17])
# print_tree(t,0)

def get_bst_postorder(bst):
    if bst is not None:
        return get_bst_postorder(bst.get_left()) + get_bst_postorder(bst.get_right()) + [bst.get_data()]
    else:
        return []

# t = BinarySearchTree(15,BinarySearchTree(2),BinarySearchTree(17,BinarySearchTree(16),BinarySearchTree(18)))
# print(get_bst_postorder(t))

def x(bst):
    if bst is not None:
        return x(bst.get_right()) + [bst.get_data()]
    else:
        return []

def get_maximum(bst):
    lists = x(bst)
    return max(lists)


# t = BinarySearchTree(15,BinarySearchTree(2),BinarySearchTree(17,BinarySearchTree(16),BinarySearchTree(18)))
# print(get_maximum(t))


def print_insert_position(bst, value):
    if bst.get_data() > value:
        if bst.get_left() is not None:
            print_insert_position(bst.get_left(),value)
        else:
            print("To the left of {}".format(bst.get_data()))
    elif bst.get_data() < value:
        if bst.get_right() is not None:
            print_insert_position(bst.get_right(),value)
        else:
            print("To the right of {}".format(bst.get_data()))
    else:
        print("Duplicate")


def is_binary_search_tree(my_tree, min_value, max_value):
    if my_tree.get_left() is not None:
        min_value = my_tree.get_left().get_data()
    if my_tree.get_right() is not None:
        max_value = my_tree.get_right().get_data()
    if my_tree.get_right() is None and my_tree.get_left() is None:
        return True
    if min_value <= my_tree.get_data() and max_value >= my_tree.get_data():
        return is_binary_search_tree(my_tree.get_right(),min_value,max_value)
    else:
        return False

# t = BinarySearchTree(1,BinarySearchTree(2),BinarySearchTree(17,BinarySearchTree(16),BinarySearchTree(18)))
# print(is_binary_search_tree(t,0,999))
