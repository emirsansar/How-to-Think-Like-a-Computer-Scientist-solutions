#Write a function called hypotenuse that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as parameters:

def hypotenuse(a,b):
    hypo = ( a*a + b*b ) ** (1/2)
    return hypo

print(hypotenuse(3,4))