"""author = "GARRY GY"
Date:2021-11-21
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""


class LinkedListHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = []
        self.count = 0
        for i in range(self.__size):
            self.__slots.append(LinkedList())

    def get_hash_code(self, key):
        index = key % self.__size
        return index

    def __str__(self):
        a = ''
        for i in range(len(self.__slots)):
            if i < self.__size - 1:
                a += self.__slots[i].__str__()
                a += '\n'
            else:
                a += self.__slots[i].__str__()

        return a

    def put(self, key):
        index = self.get_hash_code(key)
        self.__slots[index].add(key)
        self.count += 1

    def __len__(self):
        return self.count