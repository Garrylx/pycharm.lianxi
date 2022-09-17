"""author = "GARRY GY"
Date:2021-09-17
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
num = int(input("Enter number of rows: "))
xlist = []
for x in range(1,num+1):
    xlist.append(x)
    for y in xlist:
        if y != len(xlist):
            print(y,end=" ")
        else:
            print(y,end="")
    if x == len(xlist):
        print("")
        pass

