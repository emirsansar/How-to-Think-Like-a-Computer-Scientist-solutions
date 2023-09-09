#Write a function slope(x1, y1, x2, y2) that returns the slope of the line through the points (x1, y1) and (x2, y2).

def slope(x1,y1,x2,y2):
    length_of_x = x1-x2
    length_of_y = y1-y2

    result = length_of_y / length_of_x

    return result

print(slope(5,3,4,2))