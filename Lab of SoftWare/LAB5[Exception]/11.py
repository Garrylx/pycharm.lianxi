def read_scores(filename):
    try:
        if isinstance(filename,str) == False:
            print("ERROR: Invalid input!")
            raise TypeError
        if filename == "":
            print("ERROR: Invalid filename!")
            raise TypeError
        input_file = open(filename, "r")
        scores = input_file.read().split()
        numbers = [float(score) for score in scores if float(score) >= 0 ]
        number_of_marks = len(numbers)
        total_marks = sum(numbers)
        if numbers == []:
            print("ERROR: No positive scores in the input file.")
        else:
            print("There are {} score(s).".format(number_of_marks))
            print("The total is {:.2f}.".format(total_marks))
            print("The average is {:.2f}.".format(total_marks/number_of_marks))
        input_file.close()

    except FileNotFoundError:
        print("ERROR: The file \'{}\' does not exist.".format(filename))
    except ValueError:
        return print("ERROR: The input file contains invalid values.")
    except TypeError:
        pass


    # finally:
    #     input_file.close()
