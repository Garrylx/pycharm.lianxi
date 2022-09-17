"""author = "GARRY GY"
Date:2021-09-18
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
my_dict = {6:['monday', 'coffee', 'strong'], 5:['short'], 3:['may', 'and']}

def print_keys_values_inorder(my_dict):
    key_lists = list(my_dict.keys())
    key_lists = sorted(key_lists)
    str1 = ""
    for key in key_lists:
        for x in list(sorted(my_dict[key])):
            str1 += x
            str1 += " "
        print(str(key) + " " + str1)
        str1 = ""

