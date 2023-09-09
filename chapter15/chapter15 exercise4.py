#The equation of a straight line is “y = ax + b”, (or perhaps “y = mx + c”). The coefficients a and b completely describe the line.
# Write a method in the Point class so that if a point instance is given another point,
# it will compute the equation of the straight line joining the two points. It must return the two coefficients as a tuple of two values.

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def get_line_to(self,nokta2):
        x_length = self.x - nokta2.x
        y_length = self.y - nokta2.y

        slope = y_length / x_length
        constant_number = self.y - (slope*self.x)      # constant number is found from the line equation.

        return (slope, constant_number)

a = Point(4,11)
b = Point(6,15)

print(type(a.get_line_to(b)))
print(a.get_line_to(b))