"""author = "GARRY GY"
Date:2021-12-14
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class Stack:
    from copy import deepcopy

    def __init__(self):
        self.__items = []

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

    def __str__(self):
        return "Stack: {}".format(self.__items)

    def __len__(self):
        return len(self.__items)

    def clear(self):
        self.__items = []

def mirror_list(my_list):
    adt = Stack()
    for x in my_list:
        adt.push(x)
    while adt.is_empty() is False:
        my_list += [adt.pop()]
    return my_list

#print(mirror_list([1,2,3,4,5]))