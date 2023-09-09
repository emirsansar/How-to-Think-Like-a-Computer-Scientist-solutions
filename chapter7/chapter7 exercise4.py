#Count how many words in a list have length 5.

list = ["ahmet","mehmet","emir","5","exercise","words"]
count=0

for i in list:
    if len(i) == 5:
        count = count + 1

print("The numbers of words have length 5 is {}".format(count))