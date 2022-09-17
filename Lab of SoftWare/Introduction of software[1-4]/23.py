"""author = "GARRY GY"
Date:2021-09-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_sorted_unique_words_list(sentence):
    sen_list = sentence.split()
    for num in range(len(sen_list)):
        sen_list[num] = sen_list[num].lower()
    sen_list = sorted(list(set(sen_list)))
    return sen_list
