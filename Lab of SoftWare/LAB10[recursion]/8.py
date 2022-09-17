"""author = "GARRY GY"
Date:2021-10-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
sa = ""
def get_max_len_list(words):
    global sa
    if len(words) > 1:
        str1 = words[-1]
        words = words[:-1]
        if len(str1) > len(sa):
            sa = str1
            return get_max_len_list(words)
        else:
            return get_max_len_list(words)
    else:
        if len(words[0]) > len(sa):
            return len(words[0])
        else:
            return len(sa)

lst = ['life', 'is', 'a', 'long', 'way']
print(get_max_len_list(lst))

def get_max_len_list(words,sa=""):
    if len(words) > 1:
        str1 = words[-1]
        words = words[:-1]
        if len(str1) > len(sa):
            sa = str1
            return get_max_len_list(words,sa)
        else:
            return get_max_len_list(words,sa)
    else:
        if len(words[0]) > len(sa):
            return len(words[0])
        else:
            return len(sa)