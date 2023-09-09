#Write a function that removes all occurrences of a given letter from a string:

def remove_letter(harf,kelime):

    bos = ""

    for i in kelime:
        if i == harf:
            i = ""      # harfi boş bir karaktere dönüştürür.
            bos = bos + i
        else:
            bos = bos + i

    return bos

print(remove_letter("a", "apple"))
print(remove_letter("a", "banana"))
print(remove_letter("z", "banana"))
print(remove_letter("i", "Mississippi"))
print(remove_letter("b", ""))