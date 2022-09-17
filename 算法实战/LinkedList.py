class Node:
    def __init__(self, init_data, init_next=None):
        self.__data = init_data
        self.__next = init_next
    def get_data(self):
        return self.__data
    def get_next(self):
        return self.__next
    def set_data(self, new_data):
        self.__data = new_data
    def set_next(self, new_next):
        self.__next = new_next
    def __str__(self):
        return str(self.__data)
    def add_after(self, value):
        new_node = Node(value,self.__next)
        self.__next = new_node
    def remove_after(self):
        self.__next = self.__next.get_next()

class LinkedList:
    def __init__(self):
        self.__head = None
    def add(self, item): #add to the beginning of the list
        new_node = Node(item, self.__head)
        self.__head = new_node
    def size(self):
        current = self.__head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
    def get_head(self):
        return self.__head
    def set_head(self, new_node):
        self.__head = new_node
    def __len__(self):
        return self.size()
    def is_empty(self):
        return self.__head == None
    def __str__(self):
        result = ""
        if self.__head != None:
            current = self.__head
            while current != None:
                result = result + str(current.get_data()) + ", "
                current = current.get_next()
        return '[' + result[:-2] + ']'
    def __contains__(self,item):
        current = self.__head
        while current != None:
            if current.get_data() == item:
                return True
            else:
                current = current.get_next()
        return False

def remove_at_index(my_list, index):
    current = my_list.get_head()
    if my_list.size()-1 < index:
        pass
    else:
        while index > 1:
            current = current.get_next()
            index -= 1
        if index == 0:
            my_list.set_head(current.get_next())
        elif index == 1:
            current.remove_after()


def find_maximum(my_list):
    current = my_list.get_head()
    max_num = current.get_data()
    while current.get_next() is not None:
        current = current.get_next()
        if max_num < current.get_data():
            max_num = current.get_data()
    return max_num









ll1 = LinkedList()
ll1.add(5)
ll1.add(4)
ll1.add(3)
ll1.add(2)
ll1.add(1)
print(find_maximum(ll1))