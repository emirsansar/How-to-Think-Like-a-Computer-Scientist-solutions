# Now write the function is_odd(n) that returns True when n is odd and False otherwise. Include unit tests for this function too.

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(4))