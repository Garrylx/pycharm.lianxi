"""author = "GARRY GY"
Date:2021-11-25
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def evaluate_f(n):
    if n == 0:
        return 3
    elif n == 1:
        return 2
    else:
        return 2*(evaluate_f(n - 1)) + 3*(evaluate_f(n - 2))

print(evaluate_f(2))