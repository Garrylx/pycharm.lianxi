"""author = "GARRY GY"
Date:2021-10-25
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def count_down(n):
    if n != 0:
        print(n)
        return count_down(n-1)
    else:
        print("Go!")

count_down(3)