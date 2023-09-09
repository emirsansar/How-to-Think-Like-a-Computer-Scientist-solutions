#Now rewrite the count_letters function so that instead of traversing the string,
# it repeatedly calls the find method, with the optional third parameter to locate new occurrences of the letter being counted.

def count_letters(kelime,harf,basla):

    while basla < len(kelime):
        if kelime[basla] == harf:
            print(basla)
        basla = basla + 1

print(count_letters("banana","a",0))