"""author = "GARRY GY"
Date:2021-10-26
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_first_lower_case(word):
    if len(word) > 0:
        if word[0] == word[0].lower() and word[0].isalpha() == True:
            return word[0]
        else:
            word = word[1:]
            return get_first_lower_case(word)
    else:
        return None

print(get_first_lower_case("WELL done"))