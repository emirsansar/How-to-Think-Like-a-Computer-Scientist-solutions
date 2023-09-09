#Encapsulate

#fruit = "banana"
#count = 0
#for char in fruit:
#   if char == "a":
#       count += 1
# print(count)

#in a function named count_letters, and generalize it so that it accepts the string and the letter as arguments.
#Make the function return the number of characters, rather than print the answer. The caller should do the printing.

def count_letters(kelime,harf):
    count = 0

    for i in kelime:
        if i == harf:
            count = count + 1
    return count

print(count_letters("banana","a"))