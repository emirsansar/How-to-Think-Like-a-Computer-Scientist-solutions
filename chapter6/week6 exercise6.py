#Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore leap years:

def days_in_months(month):

    if month == "January":
        return 31
    elif month == "February":
        return 28
    elif month == "March":
        return 31
    elif month == "April":
        return 30
    elif month == "May":
        return 31
    elif month == "June":
        return 30
    elif month == "July":
        return 31
    elif month == "August":
        return 31
    elif month == "September":
        return 30
    elif month == "October":
        return 31
    elif month == "November":
        return 30
    elif month == "December":
        return 31

print(days_in_months("December"))
