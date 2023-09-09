#Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar multiple of v by s. :

def scalar_mult(s, v):
    bos_liste = []

    for i in range(len(v)):
        bos_liste.append(v[i] * s)      # v' nin elemanlarını s ile çarpar sırayla.

    return bos_liste

print(scalar_mult(5, [1, 2]) )
print(scalar_mult(3, [1, 0, -1]) )
print(scalar_mult(7, [3, 0, 5, 11, 2]) )
