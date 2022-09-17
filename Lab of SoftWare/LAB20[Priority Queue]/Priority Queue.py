"""author = "GARRY GY"
Date:2021-12-02
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
class PriorityQueue(object):

    def __init__(self,binary_heap=None,size=None):
        self.__binary_heap = binary_heap
        self.__size = size
        if self.__size is None:
            self.__size = 0
        if self.__binary_heap is None:
            self.__binary_heap = [0]

    def __str__(self):
        return str(self.__binary_heap)

    def __len__(self):
        return self.__size

    def add_all(self, a_list):
        for item in a_list:
            self.__binary_heap.append(item)
            self.__size += 1

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.__binary_heap[index] < self.__binary_heap[index//2]:
                self.__binary_heap[index],self.__binary_heap[index//2] = self.__binary_heap[index//2],self.__binary_heap[index]
            index = index // 2


    def insert(self, element):
        self.__binary_heap.append(element)
        self.__size += 1
        PriorityQueue.percolate_up(self,self.__size)


    def get_smaller_child_index(self, index):
        child1 = index * 2
        child2 = index * 2 + 1
        if index*2 + 1 > self.__size:
            return index * 2
        else:
            return child1 if self.__binary_heap[child1] < self.__binary_heap[child2] else child2

    def percolate_down(self, index):
        while index * 2 + 1 <= self.__size:
            index_l = index * 2
            index_r = index * 2 + 1
            if self.__binary_heap[index] < self.__binary_heap[index_l] or self.__binary_heap[index] < self.__binary_heap[index_r]:
                if self.__binary_heap[index_l] < self.__binary_heap[index_r]:
                    self.__binary_heap[index], self.__binary_heap[index_l] = self.__binary_heap[index_l], self.__binary_heap[index]
                    index = index_l
                else:
                    self.__binary_heap[index], self.__binary_heap[index_r] = self.__binary_heap[index_r], self.__binary_heap[index]
                    index = index_r
            else:
                break

    def create_heap_fast(self, values):
        PriorityQueue.add_all(self,values)
        for x in range(1,self.__size):
            PriorityQueue.percolate_down(self,x)




# pq = PriorityQueue()
# keys = [9, 5, 8, 6, 3, 2]
# pq.create_heap_fast(keys)
# print(pq)

def heap_sort(values):
    p = PriorityQueue()
    p.add_all(values)

