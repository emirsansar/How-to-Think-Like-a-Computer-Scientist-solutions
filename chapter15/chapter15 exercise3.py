#Add a method slope_from_origin which returns the slope of the line joining the origin to the point.

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def slope_from_origin(self):
        x_axis= self.x - 0
        y_axis= self.y - 0
        slope = y_axis / x_axis

        return slope

a = Point(2,8)
b = Point(-1,3)

print(a.slope_from_origin())
print(b.slope_from_origin())