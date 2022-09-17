"""author = "GARRY GY"
Date:2021-10-20
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_position_of_highest(data, index):
    max = 0
    for i in range(index+1):
        if data[max] < data[i]:
            max = i
        else:
            pass
    return max

print(get_position_of_highest(['t', 'e', 'q', 'c', 'x', 'b', 'f', 'u', 'r', 'k'],4))