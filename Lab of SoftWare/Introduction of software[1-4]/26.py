"""author = "GARRY GY"
Date:2021-09-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_tags_frequency(list_of_tuples):
    all_tuple = []
    for item in list_of_tuples:
            all_tuple.append(item[1])
    dict_tuple = {}
    for x in all_tuple:
        dict_tuple[x] = all_tuple.count(x)
    return dict_tuple
