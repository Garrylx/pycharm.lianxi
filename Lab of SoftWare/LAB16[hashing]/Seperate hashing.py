"""author = "GARRY GY"
Date:2021-11-21
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class LinkedListHashTable(object):

    def __init__(self,size=7):
        self.__size = size
        self.__slots = []
        for i in range(self.__size):
            self.__slots.append(LinkedList())
            #  每一个位置都形成一个链表

    def get_hash_code(self,key):
        index = key % self.__size
        return index

    def __str__(self):
        a = ''
        for i in self.__slots:
            a += i.__str__()
            a += '\n'
        return a