import string

def cleanword(kelime):

    bos_kelime = ""
    for i in kelime:
        if i not in string.punctuation:
            bos_kelime += i

    return bos_kelime

def has_dashdash(kelime):

    for i in kelime:
        if i == "-":
            return True
    return False

