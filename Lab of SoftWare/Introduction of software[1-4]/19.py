"""author = "GARRY GY"
Date:2021-09-18
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
sentence = input("Enter a sentence: ")
sentence_list = sentence.split()
lengh_list = []
print_list = []
for x in sentence_list:
    lengh_list.append(len(x))
    lengh_list = list(set(lengh_list))
for num in lengh_list:
    for word in sentence_list:
        if len(word) == num:
            print_list.append(word)
    print_list[-1].rstrip()
    print_list = list(set(print_list))
    lower_print_list = []
    for x in print_list:
        lower_print_list.append(x.lower())
    lower_print_list = sorted(lower_print_list)
    lower_print_list.insert(0,str(num))
    for x in lower_print_list:
        print (x+" ",end="")
    print("")
    print_list = []


