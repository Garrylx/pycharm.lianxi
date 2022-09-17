"""author = "GARRY GY"
Date:2021-10-20
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def selection_row(data, index):
    max = 0
    for i in range(len(data)):
        if data[max] < data[i]:
            max = i
    data[index],data[max] = data[max],data[index]
    return data

print(selection_row(['e','q','c','x','b','f','u','r','k','m'],4))