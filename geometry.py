# GEO1000 - Assignment 3
# Authors:Qiuxian Wei
# Studentnumbers:5801737

import math

# __all__ leaves out _test method and only makes
# the classes available for "from geometry import *":
__all__ = ["Point", "Circle", "Rectangle"]

class Point(object):

    def __init__(self, x, y):
        """Constructor. 
        Takes the x and y coordinates to define the Point instance.
        """
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        """Returns WKT String "POINT (x y)".
        """
        return "POINT({0} {1})".format(self.x, self.y)

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.
        
        other - Point, Circle or Rectangle
        
        returns - True / False
        """
        if isinstance(other, Point):
            if str(self) == str(other):
                return True
            else:
                return False
        elif isinstance(other, Circle):
            if self.distance(other.center) <=other.radius:
                return True
            else:
                return False
        else:
            if other.ll.x<=self.x<=other.ur.x and other.ll.y<=self.y<=other.ur.y:
                return True
            else:
                return False



    def distance(self, other):
        """Returns cartesian distance between self and other Point
        """
        dist = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return dist


class Circle(object):

    def __init__(self, center, radius):
        """Constructor. 
        Takes the center point and radius defining the Circle.
        """
        assert radius > 0
        assert isinstance(center, Point)
        self.center = center
        self.radius = float(radius)

    def __str__(self):
        """Returns WKT str, discretizing the boundary of the circle 
        into straight line segments
        """
        N = 400
        step = 2 * math.pi / N
        pts = []
        for i in range(N):
            pts.append(Point(self.center.x + math.cos(i * step) * self.radius, 
                             self.center.y + math.sin(i * step) * self.radius))
        pts.append(pts[0])
        coordinates = ["{0} {1}".format(pt.x, pt.y) for pt in pts]
        coordinates = ", ".join(coordinates)
        return "POLYGON (({0}))".format(coordinates)

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.
        
        other - Point, Circle or Rectangle
        
        Returns - True / False
        """
        if isinstance(other, Point):
            return other.intersects(self)
        elif isinstance(other, Circle):
            if self.center.distance(other.center)<=self.radius+other.radius:
                return True
            else:
                return False
        else:
            pt_1 = Point(other.ll.x, other.ur.y)
            pt_2 = Point(other.ur.x, other.ll.y)
            c1 = Circle(pt_1, self.radius)
            c2 = Circle(other.ll, self.radius)
            c3 = Circle(other.ur, self.radius)
            c4 = Circle(pt_2, self.radius)
            r1 = Rectangle(Point(other.ll.x-self.radius, other.ll.y), pt_1)
            r2 = Rectangle(pt_1, Point(other.ur.x, other.ur.y+self.radius))
            r3 = Rectangle(pt_2, Point(other.ur.x+self.radius, other.ur.y))
            r4 = Rectangle(Point(other.ll.x, other.ll.y-self.radius), pt_2)
            return self.center.intersects(c1) or self.center.intersects(c2) or self.center.intersects(c3) or self.center.intersects(c4) \
                or self.center.intersects(r1) or self.center.intersects(r2) or self.center.intersects(r3) or self.center.intersects(r4) \
                or self.center.intersects(other)



class Rectangle(object):

    def __init__(self, pt_ll, pt_ur):
        """Constructor. 
        Takes the lower left and upper right point defining the Rectangle.
        """
        assert isinstance(pt_ll, Point)
        assert isinstance(pt_ur, Point)
        self.ll = pt_ll
        self.ur = pt_ur

    def __str__(self):
        """Returns WKT String "POLYGON ((x0 y0, x1 y1, ..., x0 y0))"
        """
        pt_1 = Point(self.ll.x, self.ur.y)
        pt_2 = Point(self.ur.x, self.ll.y)
        pts = [self.ll, pt_1, self.ur, pt_2, self.ll]
        coordinates = ["{0} {1}".format(pt.x, pt.y) for pt in pts]
        coordinates = ", ".join(coordinates)
        return "POLYGON (({0}))".format(coordinates)


    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.
        
        other - Point, Circle or Rectangle
        
        Returns - True / False
        """
        if isinstance(other, Point):
            return other.intersects(self)

        elif isinstance(other, Circle):
            return other.intersects(self)

        else:
            dist_x =  max(self.ur.x, other.ur.x) - min(self.ll.x, other.ll.x)
            dist_y =  max(self.ur.y, other.ur.y) - min(self.ll.y, other.ll.y)
            dist_w = self.width() + other.width()
            dist_h = self.height() + other.height()
            if dist_x <= dist_w and dist_y <= dist_h:
                return True
            else:
                return False



    def width(self):
        """Returns the width of the Rectangle.
        
        Returns - float
        """
        w = self.ur.x - self.ll.x
        return w

    def height(self):
        """Returns the height of the Rectangle.
        
        Returns - float
        """
        h = self.ur.y - self.ll.y
        return h


def _test():
    """Test whether your implementation of all methods works correctly.
    """
    pt0 = Point(0, 0)
    pt1 = Point(0, 0)
    pt2 = Point(10, 10)
    assert pt0.intersects(pt1)
    assert pt1.intersects(pt0)
    assert not pt0.intersects(pt2)
    assert not pt2.intersects(pt0)

    c = Circle(Point(-1, -1), 1)
    r = Rectangle(Point(0,0), Point(10,10))
    assert not c.intersects(r)

    # Extend this method to be sure that you test all intersects methods!
    # Read Section 16.5 of the book if you have never seen the assert statement


if __name__ == "__main__":
    _test()

