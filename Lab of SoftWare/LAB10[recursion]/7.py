"""author = "GARRY GY"
Date:2021-10-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
num = -999999
def get_max_list(numbers):
    global num
    if len(numbers) > 1:
        str1 = numbers[-1]
        numbers = numbers[:-1]
        if str1 > num :
            num = str1
            return get_max_list(numbers)
        else:
            return get_max_list(numbers)
    else:
        if numbers[0] > num:
            return numbers[0]
        else:
            return num

print(get_max_list([1,2,3,4,5]))