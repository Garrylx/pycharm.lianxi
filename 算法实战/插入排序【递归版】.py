"""Author = GARKAX GY
Date: 2022--04
TIME FLIES!
"""

def insertion_sort_recursion(A, n):
    if n > 1:
        insertion_sort_recursion(A, n-1)
        x = A[n - 1]
        j = n - 2
        while j >= 0 and A[j] > x:
            # 右移寻找
            A[j + 1] = A[j]
            j = j - 1
        # 找到位置后赋值
        A[j + 1] = x
        str1 = '['
        for i in A[:-1]:
            str1 = str1 + str(i) + ', '
        print(str1+str(A[-1])+']')


insertion_sort_recursion([3, 1, 8, 6], 4)


