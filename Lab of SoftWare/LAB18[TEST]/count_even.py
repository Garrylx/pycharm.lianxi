"""author = "GARRY GY"
Date:2021-11-25
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def count_evens(a_list,nlt=None):
    if nlt == None:
        nlt = []
    for x in range(len(a_list)):
        if type(a_list[x]) is list:
            count_evens(a_list[x],nlt)
        if type(a_list[x]) is not list:
            if a_list[x] % 2 == 0:
                nlt.append(a_list[x])

    return len(nlt)
print(count_evens([[1], [2], [3], [4]]))