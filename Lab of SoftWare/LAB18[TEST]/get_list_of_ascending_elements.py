"""author = "GARRY GY"
Date:2021-11-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
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
        new_node = Node(value,self.__next )
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

def get_list_of_ascending_elements(my_linked_list):
    if my_linked_list.get_head() != None:
        lists = []
        head = my_linked_list.get_head()
        lists.append(head.get_data())
        while head.get_next() != None:
            head = head.get_next()
            if head.get_data() >= lists[-1]:
                lists.append(head.get_data())

        return lists
    else:
        return []

ll3 = LinkedList()
print(get_list_of_ascending_elements(ll3))