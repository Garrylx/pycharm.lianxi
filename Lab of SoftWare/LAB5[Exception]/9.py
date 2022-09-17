def get_maori_word(dictionary, word):
    try:
        values = []
        keys =  []
        for key,value in dictionary.items():
            keys.append(key)
            values.append(value)
        if word in keys:
            index_word = keys.index(word)
            return values[index_word]
        else:
            raise KeyError

    except KeyError:
        return "ERROR: {} is not available.".format(word)

dictionary ={'example': 'tauira', 'house': 'whare', 'apple': 'aporo', 'love': 'aroha', 'food': 'kai',
'hello': 'kiaora', 'work': 'mana', 'weather': 'huarere', 'greenstone': 'pounamu',
'red': 'whero', 'orange': 'karaka', 'black': 'mangu'}
print(get_maori_word(dictionary, 'house'))
print(get_maori_word(dictionary, 'tooth'))
