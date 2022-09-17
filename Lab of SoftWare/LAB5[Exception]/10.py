def get_phone(phones_dictionary, name):
    try:
        if name == " "or name == "":
            raise KeyError
        elif isinstance(name,str) == False:
            raise TypeError
        elif name not in phones_dictionary.keys():
            return "ERROR: {} is not available.".format(name)
        else:
            return phones_dictionary[name]
    except TypeError:
        return "ERROR: Invalid input!"
    except KeyError:
        return "ERROR: Invalid name!"

phones_dictionary = {'Martin':8202, 'Angela':6620, 'Ann':4947, 'Damir':2391, 'Adriana':7113, 'Andrew':5654}
print(get_phone(phones_dictionary , 'Ann'))
print(get_phone(phones_dictionary , 'Daniel'))
print(get_phone(phones_dictionary , 123))
print(get_phone(phones_dictionary , ''))