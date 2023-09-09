#The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”.
# Write a function turn_clockwise that takes one of these four compass points as its parameter,and returns the next compass point in the clockwise direction.

def turn_clockwise(point):
    if point == "N":
        return "W"
    elif point == "W":
        return  "S"
    elif point == "S":
        return "E"
    elif point == "E":
        return "N"

print(turn_clockwise("N"))