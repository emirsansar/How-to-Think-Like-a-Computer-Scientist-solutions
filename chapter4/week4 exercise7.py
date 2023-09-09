#Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n. So sum_to(10) would be 1+2+3...+10 which would return the value 55.

def sum_to(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

number = int(input("Enter an integer number: "))

result = sum_to(number)

print(result)