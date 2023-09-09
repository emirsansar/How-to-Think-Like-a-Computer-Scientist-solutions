#Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. A call to print_triangular_numbers(5) would produce the following output:

def print_triangular_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
        print(i, "\t ", sum)

print_triangular_numbers(5)