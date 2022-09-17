def get_max(numbers):
    try:
        for i in numbers:
            if isinstance(i,int) == False and isinstance(i,float) == False:
                raise ValueError
            else:
                pass

        return float(max(numbers))
    except ValueError:
        return "ERROR: Invalid number!"

print(get_max([3, 3.5, 1, 99]))