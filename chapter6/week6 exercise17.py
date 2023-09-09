#Write is_multiple to satisfy these unit tests: Can you find a way to use is_factor in your definition of is_multiple?


def is_Factor(number1, number2):
    if number1 % number2 == 0:
        return True
    else:
        return False

def is_multiple(number1,number2):
    if is_Factor(number1,number2) == True:
        return True
    else:
        return False

print(is_multiple(12,3))
print(is_multiple(12,5))
print(is_multiple(3,12))
