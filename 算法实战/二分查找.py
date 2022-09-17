"""author = "GARRY GY"
Date:2021-07-13
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""


# 二分查找前提是有序序列
def binery_search(li, val):
    left = 0
    right = len(li) - 1  # 索引值
    while left < right:  # 当有两个值相同的时候左边可能会大于右边，查找3，有俩4，mid在第一个4 的位置
        # right = mid -1 就会出现left>right
        mid = (left + right) // 2  # 整除2
        if li[mid] == val:  # 判断mid的值与目标值的关系
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


# 二分查找比线性查找效率高

def binary_search(numbers, value):
    max_index = len(numbers) - 1
    min_index = 0
    while min_index <= max_index:
        mid = (max_index + min_index) // 2
        if numbers[mid] == value:
            return mid
        # 通过比较边界值移动索引
        elif numbers[mid] > value:
            max_index = mid - 1
        elif numbers[mid] < value:
            min_index = mid + 1
        elif max_index == min_index:
            return min_index
    else:
        return -1


print(binary_search([10, 15, 20, 27, 41, 69], 11))
