"""author = "GARRY GY"
Date:2021-09-18
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
import os
filename = input("Enter the English to Maori dictionary filename: ")
word = input("Enter an English word: ")
file_list = []
filename_do = open(filename,"r")
file_list = filename_do.readlines()
# for x in range(len(file_list)-1):
#     file_list[x] = file_list[x][0:-1]

for x in file_list:
    x.strip("\n")

dict_maori_english = {}
for item in file_list:
    item_list = item.split(":")
    dict_maori_english[item_list[0]] = item_list[1]
if word in dict_maori_english.keys():
    print("'" + word + "'" + " is translated into " + "'" + dict_maori_english[word] + "'.")
else:
    print("Sorry that word doesn't exist in Maori!")

filename_do.close()