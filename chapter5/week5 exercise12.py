#Extend the above program so that the sides can be given to the function in any order.

def is_rightangled():
    a = int(input("Enter the first side: "))
    b = int(input("Enter the second side: "))
    c = int(input("Enter the third side: "))

    if ( a*a + b*b == c*c or a*a == b*b + c*c or b*b == a*a + c*c ):
        return True
    else:
        return False

deger = is_rightangled()

print(deger)