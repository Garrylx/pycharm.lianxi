"""author = "GARRY GY"
Date:2021-09-23
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def print_all_phrases(tags_dictionary):
    for part_one in tags_dictionary["DT"]:
        for part_two in tags_dictionary["JJ"]:
            for part_three in tags_dictionary["NN"]:
                print(part_one + part_two + part_three)
