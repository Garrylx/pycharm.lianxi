"""author = "GARRY GY"
Date:2021-09-22
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
def get_sorted_unique_words_list(sentence):
    sen_list = sentence.split()
    for num in range(len(sen_list)):
        sen_list[num] = sen_list[num].lower()
    sen_list = sorted(list(set(sen_list)))
    return sen_list


def get_word_tag_tuple(tags_dictionary, search_word):
    tag_list = []
    for x in list(tags_dictionary.values()):
        if search_word in x:
            tag_list = x
            indx = list(tags_dictionary.keys())[list(tags_dictionary.values()).index(x)]

            return (search_word,indx)

def get_tag_tuple_list(tags_dictionary, sentence):
    word_lists = get_sorted_unique_words_list(sentence)
    word_list = []
    for word in word_lists:
        word_list.append(get_word_tag_tuple(tags_dictionary,word))
    return word_list