#Write a function area_of_circle(r) which returns the area of a circle of radius r.

def area_of_circle(r):
    pi = 3.14
    area = pi*pow(r,2)
    return area

radius = float(input("Enter the radius of the circle: "))

result = area_of_circle(radius)

print(result)