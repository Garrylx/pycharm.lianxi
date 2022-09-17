def get_volume(radius, height):
    types = [float,int]
    try:
        if type(radius) in types and type(height) in types:
            if radius < 0 and height < 0:
                return "ERROR: Height and radius must be positive."
            elif height < 0:
                return "ERROR: Height must be positive."
            elif radius < 0:
                return "ERROR: Radius must be positive."
            elif radius == 0 or height == 0:
                return "ERROR: Not a cylinder."
            else:
                if type(radius) == float and type(height) == float:
                    return int(3.14*radius**2*height)+1
                else:
                    return int(3.14*radius**2*height)
        else:
            raise TypeError
    except ValueError:
        pass
    except TypeError:
        return "ERROR: Invalid input."

print(get_volume(10.5,2.5))
print(get_volume(10,-2))
print(get_volume(-10,2))
print(get_volume(-10,-2))
print(get_volume(10,0))
print(get_volume(0,2))
print(get_volume(10,"a"))