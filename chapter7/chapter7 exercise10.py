# Write a function, is_prime, which takes a single integer argument and returns True when the argument is a prime number and False otherwise.

def is_prime(n):
    if n>=2:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

print(is_prime(5))
print(is_prime(8))