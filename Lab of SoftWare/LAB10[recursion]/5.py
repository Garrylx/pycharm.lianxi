"""author = "GARRY GY"
Date:2021-10-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""

def count_consonants(word):
    xlist = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    if len(word) > 0:
        str1 = word[0]
        if str1.lower() in xlist:
            word = word[1:]
            return len(str1) + count_consonants(word)
        else:
            word = word[1:]
            return count_consonants(word)
    else:
        return 0

print(count_consonants("AEIOU"))
