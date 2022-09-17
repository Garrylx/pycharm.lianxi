"""author = "GARRY GY"
Date:2021-10-25
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

def copy_string(word):
    str1 = word[:1]
    word = word[1:]
    if len(word) > 0:
        return copy_string(word) + str1
    if len(word) == 0:
        return str1

print(copy_string("hello"))