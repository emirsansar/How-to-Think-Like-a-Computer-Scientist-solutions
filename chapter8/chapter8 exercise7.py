#Write a function that reverses its string argument, and satisfies these tests:

def reverse(string):
    bos = ""

    for i in string[::-1]:   # en sondan başlayıp birer birer harfleri bos' a aktarır
        bos = bos + i

    return bos

print(reverse("happy"))
print(reverse("Python"))
print(reverse(""))
print(reverse("a"))