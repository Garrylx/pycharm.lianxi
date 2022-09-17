"""author = "GARRY GY"
Date:2021-09-17
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
str1 = input("Enter a word: ")
lists = []
for y in str1:
    lists.append(y)

str1_list = sorted(list(set(lists)))

for x in str1_list:
    print(x + ":" + str(ord(x)))