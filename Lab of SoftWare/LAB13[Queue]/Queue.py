"""author = "GARRY GY"
Date:2021-11-08
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

class IndexError(Exception):
    def __init__(self):
        pass
    def __str__(self):
        return "ERROR: The queue is empty!"

class Queue(object):
    def __init__(self):
        self.__items = []

    def is_empty(self):
        if self.__items == []:
           return True

    def enqueue(self, item):
        self.__items.insert(0,item)

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
            return self.__items[len(self.__items)-1]
    def __str__(self):
        return "Queue: {}".format(self.__items)

    def __len__(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

    def enqueue_list(self, a_list):
        for x in a_list:
            self.__items.append(x)

    def multi_dequeue(self, number):
        if len(self.__items) >= number:
            self.__items = self.__items[number:]
            return True
        else:
            return False

class Stack:
    from copy import deepcopy

    def __init__(self):
        self.__items = []

    def get_items(self):
        return self.__items

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items == []:
            raise IndexError
        return self.__items.pop()

    def peek(self):
        if self.__items == []:
            raise IndexError
        return self.__items[len(self.__items) - 1]


def mirror_queue(a_queue):
    stack1 = Stack()
    for x in a_queue.get_items():
        stack1.push(x)
    while stack1.size() != 0:
        a_queue.enqueue(stack1.pop())

def is_palindrome(word):
    q = Queue()
    S = Stack()
    for letter in word:
        q.enqueue(letter)
        S.push(letter)
    while len(q) != 0:
        if q.peek() == S.peek():
            q.dequeue()
            S.pop()
        else:
            q.dequeue()
            S.pop()
            return False
    return True

print(is_palindrome("nxyn"))

