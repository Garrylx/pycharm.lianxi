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

class LinkedList:
    def __init__(self):
        self.__head = None
        self.list = []

    def add(self, value):
        node = Node(value)
        self.list = [value] + self.list
        if self.__head == None:
            self.__head = node
        else:
            prenode = self.__head
            self.__head = node
            self.__head.set_next(prenode)

    def size(self):
        a = self.__head
        if a is None:
            return 0
        else:
            count = 1
            while a.get_next() is not None:
                a = a.get_next()
                count += 1
            return count

    def get_head(self):
        return self.__head

    def clear(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def __len__(self):
        return self.size()

    def __str__(self):
        s = '['
        for i in range(len(self.list)):
            va = str(self.list[i])
            if i != len(self.list) - 1:
                s += va
                s += ', '
            else:
                s += va

        return s + ']'

    def __contains__(self, va):
        string = self.__str__()
        if str(va) in string:
            return True
        else:
            return False

    def __getitem__(self, index):
        return self.list[index]

    def add_all(self, a_list):
        for i in a_list:
            self.add(i)

    def get_min_odd(self):
        min_n = 999
        for i in self.list:
            if i % 2 == 1 and i < min_n:
                min_n = i
        return min_n

    def reverse(self):
        res = []
        for i in self.list:
            res = res + [i]
        self.list = res

    def print_list(self):
        print("linked_list:")
        str1 = '['
        for i in range(len(self.list)):
            if i != len(self.list)-1:
                str1 = str1 + str(self.list[i]) + ", "
            else:
                print(str1 + str(self.list[i]) + "]")




9


class SquareNumber:
    def __init__(self, count=5):
        self.__count = count

    def __iter__(self):
        return SquareNumberIterator(self.__count)


class SquareNumberIterator:
    def __init__(self, count):
        self.__current = 1
        self.__count = count

    def __next__(self):
        if self.__current > self.__count:
            raise StopIteration
        else:
            a = self.__current
            self.__current += 1
            return a ** 2


10


class LinkedListIterator:
    def __init__(self, head):
        self.__current = head

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        else:
            a = self.__current.get_data()
            self.__current = self.__current.get_next()
            return a





