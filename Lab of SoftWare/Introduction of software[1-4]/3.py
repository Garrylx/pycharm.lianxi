"""author = "GARRY GY"
Date:2021-09-17
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
str1 = input("Enter a sentence: ")
str2 = ""
for num in range(len(str1)):
    if str1[num].isupper() == True:
        str2 += str1[num].lower()
    else:
        str2 += str1[num].upper()
print(str2)