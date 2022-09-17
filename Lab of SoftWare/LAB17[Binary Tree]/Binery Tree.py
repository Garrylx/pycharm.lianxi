"""author = "GARRY GY"
Date:2021-11-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class BinaryTree(object):

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self,value):
        self.left = BinaryTree(value)

    def insert_right(self,value):
        self.right = BinaryTree(value)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

def create_a_tree():
    root = BinaryTree(9,BinaryTree(3,BinaryTree(2),BinaryTree(7)),BinaryTree(6,BinaryTree(8),BinaryTree(2)))
    alp = BinaryTree("a",BinaryTree("b",None,BinaryTree("c")),BinaryTree("d",None,BinaryTree("e")))
    # return alp
    return root

x = x = create_a_tree()

def get_height(t):
    if t == None:
        return -1
    else:
        return 1 + max(get_height(t.get_left()),get_height(t.get_right()))

# print(get_height())

def count_nodes(t,f=1):
    if t == None:
        return -1
    else:
        return f + 2 + count_nodes(t.get_left(),0) + count_nodes(t.get_right(),0)

# print(count_nodes(x))

def pre_search(tree):
    if tree == None:
        return []
    else:
        return [tree.get_data()] + pre_search(tree.get_left()) + pre_search(tree.get_right())

def search(tree,ch):
    node_list = pre_search(tree)
    return True if ch in node_list else False

# print(search(x,8))

def get_max(b_tree, db):
    node_list = pre_search(b_tree)
    return max(node_list) if db == True else node_list[[ord(i[0]) for i in node_list].index(max([ord(i[0]) for i in node_list]))]

# print(get_max(x,False))

def is_full(mt):
    if mt is not None:
        if mt.get_left() is None and mt.get_right() is not None:
            return False
        if mt.get_right() is None and mt.get_left() is not None:
            return False
        return is_full(mt.get_left()) and is_full(mt.get_right())
    else:
        return True

# print(is_full(x))

def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data()))
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1)
    if tree.get_right() != None:
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)

def create_tree_from_nested_list(a_list):
    for x in range(len(a_list)):
        if type(a_list[x]) is list:
            a_list[x] = create_tree_from_nested_list(a_list[x])
        if type(x) is not list:
            pass
    return BinaryTree(a_list[0],a_list[1],a_list[2])

# t = create_tree_from_nested_list([10, [5, None, None], [15, [11, None, None], [22, None, None]]])

def convert_tree_to_list(b_tree):
    if b_tree is None:
        return None
    else:
        return [b_tree.get_data()] + [convert_tree_to_list(b_tree.get_left())] + [convert_tree_to_list(b_tree.get_right())]

# print(convert_tree_to_list(x))



