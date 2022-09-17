"""author = "GARRY GY"
Date:2021-10-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
judge = True
def no_evens(numbers):
    global judge
    if len(numbers) > 0:
        if numbers[0] % 2 == 0:
            judge = False
        else:
            numbers = numbers[1:]
            judge = True
            return no_evens(numbers)
    return judge

print(no_evens([1, 3, 5, 7]))
