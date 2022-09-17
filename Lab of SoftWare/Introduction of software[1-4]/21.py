"""author = "GARRY GY"
Date:2021-09-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_tag_words(line):
    initial_list = line.split(":")
    f_word = initial_list[0]
    s_word = sorted(initial_list[1].split())
    tuple_line = (f_word,s_word)
    return tuple_line

line = input()
print(get_tag_words(line))