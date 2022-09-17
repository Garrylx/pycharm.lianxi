"""author = "GARRY GY"
Date:2021-06-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""


def binary_search(values,item,left=0,right=0):
    mid = len(values)//2
    if left <= right:
        right = len(values)-1
        left = 0
        print(str(values[:mid])+" "+str(values[mid])+" "+str(values[mid+1:]))
        if item == values[mid]:
            return True
        elif item < values[mid]:
            right = mid-1
            return binary_search(values[:right+1],item,left,right)
        elif item > values[mid]:
            left = mid+1
            return binary_search(values[left:],item,left,right)
    else:
        return False

test_list = list(range(40))
print(binary_search(test_list, 3))
