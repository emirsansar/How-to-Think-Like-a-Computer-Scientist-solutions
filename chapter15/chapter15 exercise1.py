# Rewrite the distance function from the chapter titled Fruitful functions so that it takes two Points as parameters instead of four numbers.

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,pt2):
        x_length = (self.x - pt2.x) * (self.x - pt2.x)
        y_length = (self.y - pt2.y) * (self.y - pt2.y)

        return (x_length + y_length) ** (1/2)

a = Point(0,0)
b = Point(3,4)

print(a.distance(b))