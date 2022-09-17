def set_list_element(a_list,index,value):
    try:
        if isinstance(a_list,list) == True and isinstance(index,int):
            # if len(a_list)-1 < index:
            #     raise IndexError
            # else:
                a_list[index] = value
        else:
            raise ValueError
    except IndexError:
        return print("ERROR: Invalid index: {}.".format(index))
    except ValueError:
        return print("ERROR: Invalid input.")

list1 = [1, 2, 3]
set_list_element (list1, 4, 10);
print(list1)