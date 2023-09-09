#Write a function dot_product(u, v) that takes two lists of numbers of the same length, and returns the sum of the products of the corresponding elements of each (the dot_product).

def dot_product(u , v):
    toplam = 0

    for i in range(len(u)):
        toplam = toplam + (u[i] * v[i])         # hem v hem u' nun i'ninci elemanalrı çarpıp toplam' a ekler.

    return toplam

print(dot_product([1, 1], [1, 1]) )
print(dot_product([1, 2], [1, 4]) )
print(dot_product([1, 2, 1], [1, 4, 3]) )