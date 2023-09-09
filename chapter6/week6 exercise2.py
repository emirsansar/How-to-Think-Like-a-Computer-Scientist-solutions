#Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is “Sunday”. Once again, return None if the arguments to the function are not valid.

def day_name(number_of_date):

    if number_of_date ==0:
        return "Sunday"
    elif number_of_date ==1:
        return "Monday"
    elif number_of_date ==2:
        return "Tuesday"
    elif number_of_date ==3:
        return "Wednesday"
    elif number_of_date ==4:
        return "Thursday"
    elif number_of_date ==5:
        return "Friday"
    elif number_of_date ==6:
        return "Saturday"

print(day_name(8))