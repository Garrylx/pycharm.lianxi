"""author = "GARRY GY"
Date:2021-07-24
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""


# 树：一种数据结构
# 树是一种可递归定义的数据结构
# 树是有n各节点组成的集合：n = 0为一个空树 n>0 有一个根节点
# 根节点（可以分叉）；叶节点（不能分叉的节点）；树的深度（高度）【往下分了几个叉】
# 树的度：整个树最多分了几叉
# 子节点：上一层为父节点。父节点：下一层为子节点

# 二叉树：每个节点往下最多有两个柱子节点。
# 完全二叉树：叶节点只能出现在最下层和次下层并且最下面一层节点都集中在盖层最左边若干位置的二叉树
# 满二叉树：每一层节点数都达到最大值【排列序号不能有间隔】

# 完全二叉树顺序存储方式:列表存储。
# 左子节点 与 父节点关系 left = 2y+1
# 右子节点 与 父节点关系 right = 2y+2
# 左子节点为son 父节点为 (son-1)//2
# 右子节点为son 父节点为 (son-1)//2

# 堆：一种特殊的完全二叉树
# 大根堆：完全二叉树，【任意父节点都比子节点大】。
# 小根堆：完全二叉树，【任意子节点都比父节点大】
# 堆的向下调整：【当节点的左右子树都是堆但自身不是】把子节点大的与父节点替换


# 堆排序：
# 1.建立堆 2. 得到堆顶元素，为最大元素
# 3.去掉堆顶的元素，将堆最后一个元素放到堆顶，此时可以通过一次调整重新使堆有序【逐个向下比较】
# 4.对顶元素为第二大元素【上一个被挪走了】
# 5.重复步骤直到 堆变空

# def sift(li,low,high):
#     """
#
#     :param li 列表:
#     :param low 根节点的位置:
#     :param high 堆最后一个元素的位置:
#     :return:
#     """
#     i = low
#     left= 2*i + 1
#     right = left + 1
#     tmp = li[low] # 储存堆顶元素【一直比较】
#     while left <= high:  # 没有越界【超过最下面】
#         if li[left+1] > li[left] and left+1 <= high: # if right is bigger and exist
#             left += 1 # left标记右移一个
#         if tmp < li[left]:  #  进行完左右节点的比较后进行堆顶元素与max的比较，如果下面的值大
#             li[i] = li[left] # 替换
#             i = left # 调整堆顶元素索引，向下层移动一个
#             left = 2*i + 1 # 调整子树的节点值，向下一个
#         else:
#             li[left] = tmp # 如果堆顶的值大，把值直接放在left位置上
#             break
#     else:
#         li[left] = tmp # 如果越界了 ，上面else的语句就没有执行，最后还要把tmp值放入空位
#
# # 构造堆
# def build(li):
#     n = len(li)
#     for i in range((n - 2) // 2, -1, -1):  # 倒着一直到最上层,即每一次把最后一个元素放在顶端
#         sift(li, i, n - 1)  # 构造堆
#     # 建立完成
#
#
# def shift_sort(li):
#     n = len(li)
#     for i in range((n-2)//2,-1,-1): # 倒着一直到最上层,即每一次把最后一个元素放在顶端
#         sift(li,i,n-1) # 构造堆
#     # 建立完成
#
#     for i in range(n-1,-1,-1):
#         li[0],li[i] = li[i],li[0]
#         sift(li,0,i-1) # i-1 是新的 high
#
# li = [12, 3, 4, 7, 6, 13, 1, 10, 9, 8, 14]
# shift_sort(li)
# print(li)


# li = [i for i in range(100)]
# import  random
# random.shuffle(li) # 建立无序列表
#
# # 时间复杂度O（nlogn）
#
# # python内置模块 heapq
# import heapq
#
#
#
# heapq.heapify(li)# 建堆
# heapq.heappop(li)# 弹出最小的元素

# 大根堆
def heapify(arr, n, i):
    # 构建大顶堆
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:  # 如果没有进行上面两次的if那么largest就会==i就不会继续递归
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    # 构建大顶堆
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        # 一个个交换元素
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)
    return arr


# arr = heapSort([2,65,54,2,8,3,0,4,12])
# print(arr)


# 小根堆
# ---------------------------最小堆---------------------------------------------------
class MinHeap:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        str1 = ""
        for x in self.data[:len(self.data) - 1]:
            str1 += str(x) + ", "
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

    def heapsort(self):
        for i in range(len(self.data) - 1, 0, -1):
            # 一个个交换元素
            self.data[i], self.data[0] = self.data[0], self.data[i]  # 交换
            self.heapify(self.data, i, 0)
        return self.data


h = MinHeap()
h.build([12, 3, 4, 7, 6, 13, 1, 10, 9, 8, 14])
print(h.heapsort()[::-1])
# h.insert(11)
# print(h)
# x = h.delete_min()
# print(x)
# print(h)

# h = minheap()
# print(h)
# h.insert(1)
# print(h)
# h.insert(2)
# print(h)
# h.insert(3)
# print(h)
# print(h.delete_min())
# print(h)
# h.delete_min()
# h.delete_min()
# h.delete_min()
