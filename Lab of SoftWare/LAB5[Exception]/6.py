def get_sum_even(numbers):
    even = 0
    for num in numbers:
        try:
            if num % 2 == 0:
                even += num
            else:
                pass
        except TypeError:
            pass
    return even

print(get_sum_even(['NA']))