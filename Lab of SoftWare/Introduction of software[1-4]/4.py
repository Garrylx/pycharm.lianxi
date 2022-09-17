"""author = "GARRY GY"
Date:2021-09-17
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
# alpha1 = input("Enter a word: ")
# alpha2 = input("Enter another word: ")
# alpha1_list = alpha1.split()
# alpha2_list = alpha2.split()
# for item in alpha1_list:
#     if item in alpha2_list:
#         judge = True
#     else:
#         judge = False
# if judge == True:
#     print(alpha1 + " and " + alpha2 + " are anagrams of each other.")
# else:
#     print(alpha1 + " and " + alpha2 + " are not anagrams of each other.")


alpha1 = input("Enter a word: ")
alpha2 = input("Enter another word: ")
alist = []
blist = []
for i in alpha1:
    alist.append(i)
for j in alpha2:
    blist.append(j)
alist.sort()
blist.sort()
if alist == blist:
    print(alpha1 + " and " + alpha2 + " are anagrams of each other.")
else:
    print(alpha1 + " and " + alpha2 + " are not anagrams of each other.")
