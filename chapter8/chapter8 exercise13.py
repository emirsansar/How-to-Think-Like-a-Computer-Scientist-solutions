#Write a function that removes all occurrences of a string from another string:

def remove(s, word):

   if word.find(s) not in range(0, len(word)):
      return word
   return word[0:word.find(s)] + word[word.find(s) + len(s):]


def remove_all(s, word):
   temp = remove(s, word)

   while remove(s, temp) != temp:
      temp = remove(s, temp)
   return temp

print(remove_all("me","mehmet"))
print(remove_all("an", "banana"))
print(remove_all("cyc", "bicycle"))
print(remove_all("iss", "Mississippi"))
print(remove_all("eggs", "bicycle"))

"""
def remove_all(aranan, kelime):
   uzunluk = len(aranan)

   while True:

      if aranan in kelime:
         for i in range(0, len(kelime)):
            if aranan == kelime[i:i + uzunluk]:
               kelime = kelime[:i] + kelime[i + uzunluk:]
      else:
         break

   return kelime


print(remove_all("me", "mehmet"))
print(remove_all("an", "banana"))
print(remove_all("cyc", "bicycle"))
print(remove_all("iss", "Mississippi"))
print(remove_all("eggs", "bicycle")) """


