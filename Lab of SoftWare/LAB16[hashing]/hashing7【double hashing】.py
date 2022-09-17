"""author = "GARRY GY"
Date:2021-11-21
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

class DoubleHashTable:
    def __init__(self, size=7, second=5):
        self.__size = size
        self.second = second
        self.__slots = [None] * self.__size
        self.count = 0
        self.list = []

    def get_size(self):
        return self.__size

    def __str__(self):
        return str(self.__slots)

    def get_hash_code(self, key):
        return key % self.get_size()

    def get_new_hash_code_double_probing(self, key):
        return self.second - (key % self.second)

    def put(self, key):
        if self.count < self.__size:
            index = self.get_hash_code(key)
            first_num = index
            step_size = self.get_new_hash_code_double_probing(key)
            #  把第一次hashing值当做步进
            step = 1
            # 设置初始值步进值
            while self.__slots[index] is not None:
                index = (first_num + step * step_size) % self.__size
                # 每次更新step和index值：初始的index加上每次步进的值
                step += 1
            self.__slots[index] = key
            self.count += 1
            self.list += [key]
        elif self.count == self.__size:
            raise IndexError('ERROR: The hash table is full.')