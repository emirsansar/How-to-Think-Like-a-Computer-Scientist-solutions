#Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a function which is given the day number, and it returns the day name (a string).

gun = int(input("Enter the number of days from 0 to 6: "))

def days(n):
    if (n == 0):
        print("Sunday.")
    elif (n == 1):
        print("Monday.")
    elif (n == 2):
        print("Tuesday.")
    elif (n == 3):
        print("Wednesday.")
    elif (n == 4):
        print("Thursday.")
    elif (n == 5):
        print("Friday.")
    elif (n == 6):
        print("Saturday.")
    else:
        print("You entered the wrong number.")

days(gun)