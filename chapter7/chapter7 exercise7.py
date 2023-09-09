#Add a print function to Newton’s sqrt function that prints out better each time it is calculated. Call your modified function with 25 as an argument and record the results.

def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better

print(sqrt(30))