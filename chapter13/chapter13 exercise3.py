#Write a program that reads a text file and produces an output filem which is a copy of the file, except the first five columns of each line contain a four digit line number,
# followed by a space. Start numbering the first line in the output file at 1. Ensure that every line number is formatted to the same width in the output file.

old = open("old_3.txt","r")
new = open("new.txt","w")

rows = old.readlines()
row_no = 1

for i in rows:
    new.write(str(row_no) + " " + i[5:])       # satır numarası ve boşluk ekler. ardından "eski" dosyadaki ilk 5 sütunu almayıp geri kalan sütunları yazar.
    row_no = row_no+1

old.close()
new.close()