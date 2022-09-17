
class CircularQueue(object):

    def __init__(self,items=8,front=0,back=-1,count=0):
        self.__items = items
        self.__front = front
        self.__count = count
        self.__back = items-1
        self.__items = [None for x in range(items)]


    def is_empty(self):
        if all([x is None for x in self.__items]):
            return True
        else:
            return False

    def __str__(self):
        return "{}, front:{}, back:{}, count:{}".format(self.__items,self.__front,self.__back,self.__count)

    def is_full(self):
        if None not in self.__items:
            return True
        else:
            return False

    def enqueue(self, item=None):
        if self.is_full() == True and item == None:
            raise IndexError("ERROR: The queue is full.")
        else:
            if self.is_full() == False:
                for x in range(len(self.__items)):
                    if self.__items[x] == None:
                        self.__count += 1
                        self.__items[x] = item
                        self.__back = self.__items.index(item)
                        break
            else:
                if self.__back == len(self.__items) - 1:
                    self.__back = 0
                    self.__count += 1
                    self.__items[self.__back] = item
                else:
                    self.__back += 1
                    self.__count += 1
                    self.__items[self.__back] = item


    def dequeue(self,item=None):
        if item == None:
            self.__count -= 1
            if self.__front != len(self.__items) - 1:
                self.__front += 1
            else:
                self.__front = 0
            if self.is_empty() == True or self.__count == -1:
                raise IndexError("ERROR: The queue is empty.")
            return self.__items[self.__front-1]
        else:
            if self.is_empty() == True:
                raise IndexError("ERROR: The queue is empty.")
            else:
                return self.__items[self.__front]


    def print_all(self):
        if self.__back < self.__front:
            for i in self.__items[self.__front:]:
                if i != None:
                    print(i,end=" ")
            for i in self.__items[:self.__back+1]:
                if i != self.__items[self.__back] and i != None:
                    print(i,end=" ")
                elif i == self.__items[self.__back] and i != None:
                    print(i)
        elif self.__back == self.__front:
            print(self.__items[self.__front])
        else:
            for i in range(len(self.__items)):
                if i >= self.__front and self.__items[i] != None:
                    if i != self.__back:
                        print(self.__items[i],end=" ")
                    else:
                        print(self.__items[i])





