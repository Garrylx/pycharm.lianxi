"""author = "GARRY GY"
Date:2021-07-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
import random

# 快速排序框架
# 取一个元素，让左边的元素都比它小，右边的都比它大
def quick_sort(data,left,right):
    if left < right:
        mid = partition(data,left,right)
        quick_sort(data,left,mid-1) # 中间值的左边部分
        quick_sort(data,mid+1,right) # 中间值的右边部分
    print(data)

# 主函数
# 从左边拿一个比res小的放在右边，左边出现一个空位，再从右边选一个比res值大的放在左边，右边出现空位
# 当左边与右边的索引重合时把res放在索引位置

def partition(data,left,right):
    # right left为索引
    tmp = random.choice(data)
    # 解决初始全部倒序问题
    data[0], tmp = tmp, data[0]
    while left < right:
        # 判断left right是否相遇
        while data[right] >= tmp and left < right:
            # 从右边开始找比目标值大就向左移动一个索引
            right -= 1
            # 右边索引往左一位
        data[left] = data[right]
        # 把右边比tmp小的 值移动到左边【把right位置的数放在left】

        while data[left] <= tmp and left < right:
            left += 1
            # 左边索引往右一位

        data[right] = data[left]
        # 同上

    data[left] = tmp
    # 把目标值放在中间【left与right为同一个值】
    return left
    # 或right【重合了】




lis = [2,3,7,1,3,8,33,7,0,333]
quick_sort(lis,0,len(lis)-1)

# 复杂度n * logn
# 缺点： 属于递归算法，python有最大递归深度，而且占用大量内存
# 缺点： 最坏情况：倒序的数列。 解决：随机找一个数替换第一个数字