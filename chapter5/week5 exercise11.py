#Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled.
# Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

def is_rightangled(a,b,c):
    if ( a*a + b*b == c*c ):
        return True
    else:
        return False

deger = is_rightangled(3,4,5)

print(deger)