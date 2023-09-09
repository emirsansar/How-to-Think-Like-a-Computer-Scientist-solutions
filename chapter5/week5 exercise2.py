#You go on a wonderful holiday leaving on day number 3 (a Wednesday). You return home after 137 sleeps.
# Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

kac_gun = int(input("How long will you spend time on holiday? "))

def which_day(k):
    long = (k % 7)
    n = 0

    if long == n:
        print("You will return on Wednesday. ")
    elif long == n+1:
        print("You will return on Thursday. ")
    elif long == n+2:
        print("You will return on Friday. ")
    elif long == n+3:
        print("You will return on Saturday. ")
    elif long == n+4:
        print("You will return on Sunday. ")
    elif long == n+5:
        print("You will return on Monday. ")
    elif long == n+6:
        print("You will return on Tuesday.")

which_day(kac_gun)