#Write a program that undoes the numbering of the previous exercise: it should read a file with numbered lines and produce another file without line numbers.

old = open("new.txt","r")
new = open("new_2.txt","w")

rows = old.readlines()

for i in rows:
    new.write(i[3:])    # skips the number and space columns in "new.txt" from the previous exercise and writes the rest.

old.close()
new.close()