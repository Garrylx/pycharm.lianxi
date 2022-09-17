def is_valid_radius(score):
    try:
        if isinstance(score,int) == True or isinstance(score,float) == True:
            if  score >= 0:
                return True
            else:
                raise ValueError
        else:
            raise ValueError

    except ValueError:
        return "ERROR: Invalid score!"

print(is_valid_radius(-1))