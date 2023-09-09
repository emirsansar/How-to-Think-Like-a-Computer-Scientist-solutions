#What will num_digits(0) return? Modify it to return 1 for this case. Why does a call to num_digits(-24) result in an infinite loop? (hint: -1//10 evaluates to -1)
# Modify num_digits so that it works correctly with any integer value.

def num_digits(n):
    count = 0

    if n == 0:
        return 1
    if n<=0:
        n = n * (-1)

    while n != 0:
        count = count + 1
        n = n // 10
    return count

print(num_digits(0))
print(-1//10)
print(-1/10)
print(45//10)
print(-15//10)
print(num_digits(-12345))
