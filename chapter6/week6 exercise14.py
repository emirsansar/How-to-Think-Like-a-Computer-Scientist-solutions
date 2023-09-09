# Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(3))
print(is_even(4))