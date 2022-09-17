"""author = "GARRY GY"
Date:2021-11-21
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class SimpleHashTable:
    def __init__(self,size=7):
        self.__size = size
        self.__slots = [None]*self.__size
        self.count = 0
        self.list = []

    def get_size(self):
        return self.__size

    def __str__(self):
        return str(self.__slots)

    def get_hash_code(self,key):
        return key % self.get_size()

    def get_new_hash_code_linear_probing(self,index):
        return (index+1) % self.get_size()

    def put(self,key):
        if self.count < self.__size:
            index = self.get_hash_code(key)
            while self.__slots[index] is not None:
                index = self.get_new_hash_code_linear_probing(index)
            self.__slots[index] = key
            self.count += 1
            self.list += [key]
        elif self.count == self.__size:
            raise IndexError('ERROR: The hash table is full.')

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def clear(self):
        self.__slots = [None]*self.__size
        self.count = 0

    def rehashing(self,new_size):
        self.__size = new_size
        # 形成新大小的hashing表
        num = []
        for i in self.list:
            num += [i]
        num = sorted(num)
        # 原来的hashing表进行排序
        self.list = []
        self.__slots = [None]*self.__size
        for i in num:
            self.put(i)
            # 重新录入