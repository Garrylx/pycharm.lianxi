"""Author = GARKAX GY
Date: 2022--18
TIME FLIES!
"""

class minheap:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        str1 = ""
        for x in self.data[:len(self.data)-1]:
            str1 += str(x)+", "
        return str1 + str(self.data[-1]) if self.data else ""

    def build(self, lst):
        self.data = lst
        n = len(self.data)
        for i in range(n, -1, -1):
            self.heapify(self.data, n, i)

    def insert(self, x):
        self.data = self.data + [x]
        self.build(self.data)

    def delete_min(self):
        if self.data:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            tmp = self.data.pop(-1)
            self.heapify(self.data, len(self.data), 0)
            return tmp
        else:
            print("The heap is empty!")

    def heapify(self, arr, n, node):
        min_node = node
        l = node * 2 + 1
        r = l + 1
        if l < n and arr[l] < arr[min_node]:
            min_node = l
        if r < n and arr[r] < arr[min_node]:
            min_node = r
        if min_node != node:
            arr[min_node], arr[node] = arr[node], arr[min_node]
            self.heapify(arr, n, min_node)
            # 向下一层递归

    def heapSort(self):
        for i in range(len(self.data) - 1, 0, -1):
            # 一个个交换元素
            self.data[i], self.data[0] = self.data[0], self.data[i]  # 交换
            self.heapify(self.data, i, 0)
        return self.data


def find_lowest_cost(subsystems):
    x = minheap()
    x.build(subsystems)
    subsystems = x.heapSort()[::-1]
    tmp_list = [] # 存储当前两个数相加后的值，栈结构，先入先出
    sum_list = [] # 用于寻找下一次需要相加的两个数
    final_list = [] # 储存每一次出现相加操作的相加结果值
    if len(subsystems) > 1:
        tmp = subsystems.pop(0) + subsystems.pop(0)
        tmp_list.append(tmp)
        final_list.append(tmp)
        while len(subsystems) > 0:
            if len(sum_list) != 2:
                if subsystems[0] >= tmp_list[0] and len(tmp_list) == 1:
                    tmp = subsystems.pop(0) + tmp_list.pop(0)
                    tmp_list.append(tmp)
                    final_list.append(tmp)
                elif subsystems[0] >= tmp_list[0] and len(tmp_list) == 2:
                    sum_list.append(tmp_list.pop(0))
                    if subsystems[0] >= tmp_list[0]:
                        tmp = tmp_list.pop(0) + sum_list.pop(0)
                        tmp_list.append(tmp)
                        final_list.append(tmp)
                    else:
                        tmp = subsystems.pop(0) + sum_list.pop(0)
                        tmp_list.append(tmp)
                        final_list.append(tmp)
                else:
                    sum_list.append(subsystems.pop(0))
            while len(sum_list) != 2:
                if subsystems: # 每一次必定会出现两个数相加的操作，如果原始列表没有值，那么一定在tmp和sum的List中各有一个
                    if subsystems[0] < tmp_list[0]:
                        sum_list.append(subsystems.pop(0))
                    else:
                        sum_list.append(tmp_list.pop(0))
                else:
                    sum_list.append(tmp_list[0])
            tmp = sum(sum_list)
            tmp_list.append(tmp)
            final_list.append(tmp)
            sum_list = []
        else:
            return sum(final_list)
    else:
        return 0

subsystems = [3, 10, 7, 4]
print(find_lowest_cost(subsystems))

subsystems = [100]
print(find_lowest_cost(subsystems))

subsystems = [12, 33, 1, 7, 8, 9]
print(find_lowest_cost(subsystems))


# 寻找最小中间量


"""
In this exercise, consider we are developing a software system. 
We have implemented a list of sub-systems, and now we want to integrate all these sub-systems into a single system. 
Each sub-system is associated to a non-negative cost (e.g., for code refactoring). 
The cost of integrating two sub-systems is the sum of the costs of them. Let's say each time we can only integrate two sub-systems into one,
your task is to minimize the total cost of the integrations.

For instance, assume we have a list [3, 10, 7, 4] storing the cost of each sub-system. 

In step 1, we merge 3 and 4 with cost 3 + 4 = 7.
In step 2, we merge the new system and 7 with cost 7 + 7 = 14.
In step 3, we merge the new system and 10 with cost 14 +10 = 24. 
The total cost is 7 + 14 + 24 = 45. This is the lowest cost we can achieve.

Given a list of values of n sub-systems, 
your task is to estimate the minimum total cost to integrate all systems. 
You will need to use the minheap class in the previous question. 
Copy and paste from the previous question in the answer box and complete the function find_lowest_cost(subsystems)
"""



