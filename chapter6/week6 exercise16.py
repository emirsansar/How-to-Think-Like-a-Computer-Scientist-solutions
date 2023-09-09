# Write a function is_factor(f, n). These test cases answer the question Do we treat 1 and 15 as factors of 15?

def is_Factor(number1, number2):
    if number2 % number1 == 0:
        return True
    else:
        return False

print(is_Factor(1,15))
print(is_Factor(5,12))