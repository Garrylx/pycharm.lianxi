def count_consonants(word):
    vowel = ["a","e","i","o","u"]
    consonant = []
    try:
        if isinstance(word,str)==True:
            for i in word:
                if i.isalpha() == True and i not in vowel and i not in consonant:
                    consonant.append(i)
                else:
                    pass
            return len(consonant)
        else:
            raise ValueError

    except (ValueError,AttributeError):
        return "ERROR: Invalid input!"

print(count_consonants(".1,"))