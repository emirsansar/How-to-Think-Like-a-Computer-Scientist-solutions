#Write the inverse function day_num which is given a day name, and returns its number:

def day_num(day):

    if day == "Sunday":
        return 0
    elif day == "Monday":
        return 1
    elif day == "Tuesday":
        return 2
    elif day == "Wednesday":
        return 3
    elif day == "Thursday":
        return 4
    elif day == "Friday":
        return 5
    elif day == "Saturday":
        return 6

print(day_num("Sunday"))
