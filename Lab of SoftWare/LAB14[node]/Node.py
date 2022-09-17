"""author = "GARRY GY"
Date:2021-11-11
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class Node(object):

    def __init__(self,data=None,next=None):
        self.__data = data
        self.__next = next

    def __str__(self):
        return "%s"%self.__data

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next

    def add_after(self, value):
        nx = Node(value)
        tmp = self.__next
        nx.set_next(tmp)
        self.__next = nx

    def remove_after(self):
        if self.__next.get_data() == None:
            self.__next = None
        else:
            self.__next = self.__next.get_next()

    def __contains__(self, value):
        if self.__data == value:
            return True
        else:
            if self.__next != None:
                tmp = self.__next
            else:
                return False
            while True:
                if tmp.__next != None or tmp.get_data() == value:
                    data = tmp.get_data()
                    if value == data:
                        return True
                    elif data == None:
                        return False
                    else:
                        tmp = tmp.get_next()
                else:
                    return False

    def get_sum(self):
        node_list= []
        if self.__next == None:
            return self.__data
        else:
            node_list.append(self.__data)
            tmp = self.__next
            while True:
                if tmp != None:
                    node_list.append(tmp.get_data())
                    tmp = tmp.get_next()
                else:
                    return sum(node_list)


def print_node_chain(node_of_chain):
    if node_of_chain.get_next() == None:
        print(node_of_chain.get_data())
    else:
        print(node_of_chain.get_data())
        tmp = node_of_chain.get_next()
        while 1:
            if tmp.get_next() == None:
                return print(tmp.get_data())
            else:
                print(tmp.get_data())
                tmp = tmp.get_next()


def create_node_chain(values):
    if len(values) >= 2:
        now = Node(values[0])
        next = Node(values[1])
        now.set_next(next)
        values[0] = now
        for x in range(1,len(values)):
            if x != len(values) - 1:
                now = next
                next = Node(values[x+1])
                now.set_next(next)
                values[x] = now
            else:
                values[x] = next
        return values[0]
    else:
        return Node(values[0])


def convert_to_list(first_node):
    node_list = []
    tmp = first_node
    while 1:
        if tmp.get_next() == None:
            node_list.append(tmp.get_data())
            return node_list
        else:
            node_list.append(tmp.get_data())
            tmp = tmp.get_next()



def get_consecutive_sum(first_node):
    xlist = convert_to_list(first_node)
    sum_list = []
    while xlist != []:
        sum_list.append(sum(xlist))
        xlist = xlist[1:]
    return sum_list




