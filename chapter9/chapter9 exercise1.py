#We’ve said nothing in this chapter about whether you can pass tuples as arguments to a function.
# Construct a small Python example to test whether this is possible, and write up your findings.

def sayıları_carp(numbers):   #listedeki sayıları çarpma fonksiyonu.
    result = 1
    length = len(numbers)
    for i in range(length):
        carpim = result * numbers[i]

    return result

numbers = (1,3,5)

print(sayıları_carp(numbers))