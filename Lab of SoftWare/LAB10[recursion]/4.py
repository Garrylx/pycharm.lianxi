"""author = "GARRY GY"
Date:2021-10-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def print_between(start, end):
    if start + 1 <= end:
        print(start,end=" ")
        return print_between(start+1,end)
    else:
        print(end)
        return end

print_between(1,5)