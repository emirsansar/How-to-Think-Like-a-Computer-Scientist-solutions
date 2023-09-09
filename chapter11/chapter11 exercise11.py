#Suppose you want to swap around the values in two variables. You decide to factor this out into a reusable function, and write this code:
#Run this program and describe the results. Oops! So it didn’t do what you intended! Explain why not.

"""
def swap(x, y):                                         # Incorrect version
    print("before swap statement: x:", x, "y:", y)
    (x, y) = (y, x)
    print("after swap statement: x:", x, "y:", y)   """

def swap(x, y):
    print("Before swap statement: x:", x, "y:", y)
    for i in range(len(x)):
        (x[i], y[i]) = (y[i], x[i])                     # hata bu şekilde çözülebilir. x ve y' nin i' ninci elemanalrı sırasıyla liste içinde değiştirmemiz gerekiyor.
    print("After swap statement: x:", x, "y:", y)


a = ["This", "is", "fun"]
b = [2, 3, 4]
print(" before swap function call: a:", a, "b:", b)
swap(a, b)
print(" after swap function call: a:", a, "b:", b)