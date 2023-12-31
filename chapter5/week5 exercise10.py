#Write a function find_hypot which, given the length of two sides of a right-angled triangle, returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.)

def find_hypot(x,y):
    if x>0 and y>0:
        hypotenuse = ( x*x + y*y ) ** (1/2)

    return hypotenuse

hipotenus = find_hypot(3,4)

print(hipotenus)