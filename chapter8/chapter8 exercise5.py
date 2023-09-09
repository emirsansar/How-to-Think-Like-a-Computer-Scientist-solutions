#Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text.
#Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts the number of words in your text that contain the letter “e”

def kelime_ve_e_say():
    import string

    soz = '''Eğer bir gün benim sözlerim bilimle ters düşerse bilimi seçin.'''
    bos_kelime = ""
    for k in soz:
        if k not in string.punctuation:    # noktalama işaretlerini kaldırıyor.
            bos_kelime = bos_kelime + k

    print(bos_kelime)

    ayrılmıs_soz = bos_kelime.split()       # soz' u ayrı kelimelere ayırıp liste yapıyor.

    print(ayrılmıs_soz)

    say_e = 0
    kelime_sayisi = len(ayrılmıs_soz)       # kaç kelime olduğunu buluyor.

    for i in ayrılmıs_soz:
        for k in i:      # kelime' nin içinde gezer.
            if k == "e":
                say_e = say_e + 1
                break       # aynı kelimede fazladan e varsa saymasını engeller.

    yuzde = (say_e / kelime_sayisi) * 100

    print("Your text contains {0} words, of which {1} (%{2})words contain an ""e"" .".format(kelime_sayisi,say_e,yuzde))

print(kelime_ve_e_say())