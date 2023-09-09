#Can your day_add function already work with negative deltas? For example, -1 would be yesterday, or -7 would be a week ago:

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

print(day_add(-6))

# It works with negative deltas.