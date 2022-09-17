"""author = "GARRY GY"
Date:2021-09-23
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back. """

from random import choice as cc
def print_random_phrase(tags_dictionary):
    word1 = cc(tags_dictionary["DT"])
    word2 = cc(tags_dictionary["JJ"])
    word3 = cc(tags_dictionary["NN"])
    print(word1 + " " + word2 + " " + word3)


