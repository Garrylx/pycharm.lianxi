"""author = "GARRY GY"
Date:2021-09-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_tag_words(line):
    initial_list = line.split(":")
    f_word = initial_list[0]
    s_word = sorted(initial_list[1].split())
    tuple_line = (f_word,s_word)
    return tuple_line


def create_tags_dictionary(f_list):
    f_read = open(filename, "r")
    f_list = f_read.readlines()
    for tag in range(len(f_list)):
        f_list[tag] = f_list[tag].strip('\n')
    f_read.close()

    dicts = {}
    tag_list = []
    for x in range(len(f_list)):
        tuple_line = get_tag_words(f_list[x])
        dicts[tuple_line[0]] = tuple_line[1]
        tag_list.append(tuple_line[0])
    return dicts

filename = input()
f_list = read_content(filename)
tags = create_tags_dictionary(f_list)
for key in sorted(tags):
    print(key,tags[key])
