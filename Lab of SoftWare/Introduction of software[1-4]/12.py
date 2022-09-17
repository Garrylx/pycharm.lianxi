"""author = "GARRY GY"
Date:2021-09-18
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
file_name = input("Enter filename: ")
file_exe = open(file_name,"r")
word_list = file_exe.read()
word_list = word_list.split()
longest = 0
for i in range(len(word_list)):
    if len(word_list[i]) > len(word_list[longest]):
        longest = i
    elif len(word_list[i]) == len(word_list[longest]):
        if ord(word_list[i][0]) > ord(word_list[longest][0]):
            longest = i
        else:
            pass
print('The longest word is "'+word_list[longest]+'"')
file_exe.close()