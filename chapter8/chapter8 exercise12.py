#Write a function that removes the first occurrence of a string from another string:

def remove(s, word):

   if word.find(s) not in range(0, len(word)):
      return word

   return word[0:word.find(s)] + word[word.find(s) + len(s):]

print(remove("an", "banana"))
print(remove("cyc", "bicycle"))
print(remove("iss", "Mississippi"))
print(remove("eggs", "bicycle"))

