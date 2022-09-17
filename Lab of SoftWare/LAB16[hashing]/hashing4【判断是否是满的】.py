class SimpleHashTable(object):

    def __init__(self,size=7):
        self.__size = size
        self.__slots = [None]*self.__size
        self.count = 0

    def get_size(self):
        return self.__size

    def __str__(self):
        return str(self.__slots)

    def get_hash_code(self,key):
        return key % self.get_size()

    def get_new_hash_code_linear_probing(self,index):
        return (index+1) % self.get_size()
        # 每次刷新index值【+1】

    def put(self,key):
        if self.count < self.__size:
            # hashing表是否是满的
            index = self.get_hash_code(key)
            # 第一个元素位置
            while self.__slots[index] is not None:
                index = self.get_new_hash_code_linear_probing(index)
            self.__slots[index] = key
            self.count += 1
            # 记录表内的有效数字
        elif self.count == self.__size:
            # hashing 表不是满的
            raise IndexError('ERROR: The hash table is full.')

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0
    # 简化，在表达式里最直接判断

    def clear(self):
        self.__slots = [None]*self.__size
        # 重新形成原始列表
        self.count = 0
