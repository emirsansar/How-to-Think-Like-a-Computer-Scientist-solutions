#Count how many words occur in a list up to and including the first occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)

list = ["sam","list","print","function"]
count = 0

for i in list:
    count = count + 1

print("The number of the words in the list is {}".format(count))