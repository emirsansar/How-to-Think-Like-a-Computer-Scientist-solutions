#Write a function that counts how many times a substring occurs in a string:

def count(aranan,kelime):
    sayac = 0
    aranan_uzunluk = len(aranan)

    for i in range(len(kelime)):
        if kelime[i:i+aranan_uzunluk] == aranan:        # kelime'de i ve aranan'ın uzunluğu arasındaki harfleri aranan ile kıyaslar.
            sayac = sayac + 1
    return sayac

print(count("is", "Mississippi"))
print(count("an", "banana"))
print(count("ana", "banana"))