#Given four points that fall on the circumference of a circle, find the midpoint of the circle. When will this function fail?

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print("({0}, {1})".format(self.x, self.y))

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def slope_between(self, target):
        m = (target.y - self.y) / (target.x - self.x)
        return m

    def line_equation(self, slope):
        b = self.y - slope * self.x
        return (slope, b)

    def line_perp(self, slope):
        """ Return a line through the point but perpendicular to the slope."""

class Line:
    """ Line class represents and mainpulates lines of format y = mx + b. """
    def __init__(self, m=1, b=0):
        self.m = m
        self.b = b

    def print_line(self):
        print("({0}, {1})".format(self.m, self.b))

    def intersection(self, line):
        """ Returns the intersection point of two line. """
        inter = Point(0, 0)
        inter.x = (line.b - self.b) / (self.m - line.m)
        inter.y = ((self.b * line.m) - (line.b * self.m)) / (line.m - self.m)
        return Point(inter.x, inter.y)

def find_line(point1, point2):
    """ Return the equation of a line through the given point but perpendicular to the given slope. """
    midpoint = point1.halfway(point2)
    slope = - (1 / point1.slope_between(point2))
    y_intercept = midpoint.y - (slope * midpoint.x)
    return Line(slope, y_intercept)

def find_center(a, b, c, d):

    line_1 = find_line(a, b)
    line_2 = find_line(c, d)
    return line_1.intersection(line_2)

a = Point(1, 1)
b = Point(4, 4)
c = Point(1, 4)
d = Point(4, 1)
center = Point(0,0)

center = find_center(a, b, c, d)
center.print_point()