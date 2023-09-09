#Write a function that mirrors its argument:

def mirror(string):
    bos = ""

    for i in string[::-1]:   # en sondan başlayıp birer birer harfleri bos' a aktarır
        bos = bos + i

    return string + bos

print(mirror("good"))
print(mirror("Python"))
print(mirror(""))
print(mirror("a"))
