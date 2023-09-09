#Write a function that helps answer questions like ‘“Today is Wednesday. I leave on holiday in 19 days time. What day will that be?”’
# So the function must take a day name and a delta argument — the number of days to add — and should return the resulting day name:

def day_add(number):
    mod_of_number = number % 7

    if mod_of_number == 0:
        return "Wednesay"
    elif mod_of_number == 1:
        return "Thursday"
    elif mod_of_number == 2:
        return "Friday"
    elif mod_of_number == 3:
        return "Saturday"
    elif mod_of_number == 4:
        return "Sunday"
    elif mod_of_number == 5:
        return "Monday"
    elif mod_of_number == 6:
        return "Tuesday"

print(day_add(19))