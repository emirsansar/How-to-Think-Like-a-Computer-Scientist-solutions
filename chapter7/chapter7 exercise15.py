#Write a function num_even_digits(n) that counts the number of even digits in n. These tests should pass:

def num_even_digits(n):
    count = 0

    if n == 0:
        return 1

    while n != 0:
        if n % 2 == 0:
            count = count + 1
        n = n // 10
    return count

print(num_even_digits(123456))
print(num_even_digits(2468))
print(num_even_digits(1357))
print(num_even_digits(0))