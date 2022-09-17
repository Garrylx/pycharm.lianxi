"""author = "GARRY GY"
Date:2021-09-18
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def count_consonants(str1):
    count = 0
    consonants_lists = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y"]
    for alph in str1:
        if alph.upper() in consonants_lists:
            count += 1
        else:
            pass
    return count

print(count_consonants("Hello"))