# Lists can be used to represent mathematical vectors. In this exercise and several that follow you will write functions to perform standard operations on vectors.
# Create a script named vectors.py and write Python code to pass the tests in each case.
# Write a function add_vectors(u, v) that takes two lists of numbers of the same length, and returns a new list containing the sums of the corresponding elements of each:

def add_vectors(x, y):
    empty = []

    for i in range(len(x)):
        empty.append(x[i] + y[i])

    return empty

print(add_vectors([1, 1], [1, 1]) )
print(add_vectors([1, 2], [1, 4]) )
print(add_vectors([1, 2, 1], [1, 4, 3]))