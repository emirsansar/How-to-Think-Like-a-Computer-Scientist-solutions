# Write a program that reads a file and prints only those lines that contain the substring snake.

old = open("old_2.txt","r")
snake_no = open("no_snake.txt","w")

while True:
    row = old.readline()

    if "snake" in row[:]:     # If there is a snake in the # line, it will pass.
        continue
    elif len(row[:]) == 0:
        break
    else:
        snake_no.write(row[:])

old.close()
snake_no.close()