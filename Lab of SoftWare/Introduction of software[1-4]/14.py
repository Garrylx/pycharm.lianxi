"""author = "GARRY GY"
Date:2021-09-18
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_sum_positive_even(numbers):
    sum = 0
    judge_list = []
    if numbers != []:
        for x in numbers:
            if x > 0 and x % 2 == 0:
                sum += x
                numbers.pop(x)
                judge = True
            else:
                judge_list.append(x)

        if judge_list != numbers:
            return sum
        else:
            return 0
    else:
        return 0
print(get_sum_positive_even([]))