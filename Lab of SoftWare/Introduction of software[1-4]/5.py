"""author = "GARRY GY"
Date:2021-09-17
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
str1 = ""
for x in range(200,301):
    if x % 5 == 0 and x % 3 != 0:
        x = str(x) + " "
        str1 += x
    else:
        pass
str1 = str1[0:-1]
print(str1.replace(" ",","))