def is_valid_score(score):
    try:
        if isinstance(score,int)==True or isinstance(score,float)==True:
            if 0 <= score <= 100:
                return True
            else:
                raise ValueError
        else:
            raise ValueError

    except ValueError:
        return "ERROR: Invalid score!"

print(is_valid_score(0))