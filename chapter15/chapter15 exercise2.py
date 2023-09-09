# Add a method reflect_x to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def reflect(self):
        x1 = self.x
        y1 = (-1)*self.y        #creates a new point (x1,y1)

        return Point(x1,y1)

a = Point(3,4)

print("x eksenine göre yansıması: {}".format(a.reflect()))