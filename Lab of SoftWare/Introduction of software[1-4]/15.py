"""author = "GARRY GY"
Date:2021-09-18
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_multiples_of_5(numbers):
    all_5_list = []
    same_list = []
    if numbers != []:
        for num in numbers:
            if num % 5 == 0:
                all_5_list.append(num)
            else:
                same_list.append(num)
        if same_list != numbers:
            return  all_5_list
        else:
            return []
    else:
        return []

print(get_multiples_of_5([]))