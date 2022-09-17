"""author = "GARRY GY"
Date:2021-10-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

def evaluate_m(i,n=1):

    if i > 0:
        i -= 1
        return 1/n + evaluate_m(i,n+1)
    else:
        return 0

print(evaluate_m(5))