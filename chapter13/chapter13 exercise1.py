# Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the first line in the old file becomes the last one in the new file.)

old = open("old_1.txt", "r")
ordered = open("old_1_ordered.txt","w")

rows = old.readlines()

print(rows)

for i in rows[::-1]:       # starts from the end and goes to the beginning.
    ordered.write(i)     # prints i in sequential order.

old.close()
ordered.close()