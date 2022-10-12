# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:

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
        if type(other) == Point:
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        elif type(other) == Circle:
            if math.sqrt((self.x-other.center.x)**2+(self.y-other.center.y)**2) <= other.radius:
                return True
            else:
                return False
        elif type(other) == Rectangle:
            if other.ll.x <= self.x <= other.ur.x and other.ll.y <= self.y <= other.ur.y:
                return True
            else:
                return False


    def distance(self, other):
        """Returns cartesian distance between self and other Point
        """
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)



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

        if type(other) == Circle:
            if self.center.distance(other.center) <= self.radius+other.radius:
                return True
            else:
                return False

        elif type(other)==Point:
            if other.intersects(self):
                return True
            else:
                return False
        elif type(other)==Rectangle:
            # rec_center.x=(other.pt_ll.x+other.pt_ur.x)/2
            # rec_center.y=(other.pt_ll.y+other.pt_ur.y)/2
            # dis=self.center.distance(rec_center)
            # 圆与矩形四个角点和四边是否相交
            if self.center.distance(other.ll) <= self.radius or self.center.distance(other.ur) <= self.radius or \
                math.sqrt((self.center.x - other.ll.x) ** 2 + (self.center.y - other.ur.y) ** 2) <= self.radius or \
                math.sqrt((self.center.x - other.ur.x) ** 2 + (self.center.y - other.ll.y) ** 2) <= self.radius or \
                abs(self.center.x-other.ll.x) < self.radius or abs(self.center.y-other.ll.y) < self.radius or \
                abs(self.center.x - other.ur.x)<self.radius or abs(self.center.y - other.ur.y)<self.radius \
               :
                return True
            else:
                return False




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
        return "POLYGON(({0} {1}, {2} {3}, {4} {5}, {6} {7},{0} {1}))".format(self.ll.x,self.ll.y,self.ll.x,self.ur.y, \
        self.ur.x,self.ur.y,self.ur.x,self.ll.y)

    def intersects(self, other):
        """Checks whether other shape has any interaction with
        interior or boundary of self shape. Uses type based dispatch.

        other - Point, Circle or Rectangle
        
        Returns - True / False
        """
        if type(other)==Point:
            if other.intersects(self):
                return True
            else:
                return False
        elif type(other)==Circle:
            if other.intersects((self)):
                return True
            else:
                return False
        elif type(other)==type(self):
            if self.ll.x<other.ur.x or self.ll.y<other.ur.y or other.ll.x<self.ur.x or other.ll.y<self.ur.y :
                return True
            else:
                return False


    def width(self):
        """Returns the width of the Rectangle.
        
        Returns - float
        """
        return self.ur.x-self.ll.x


    def height(self):
        """Returns the height of the Rectangle.
        
        Returns - float
        """
        return self.ur.y-self.ll.y



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
    p_ll=Point(0,0)
    p_ur=Point(1,1)
    rec=Rectangle(p_ll,p_ur)
    print(rec.__str__())
    print(type(rec))
    C1=Circle(p_ur,5)
    print(C1.__str__())
    if rec.intersects(C1):
        print('Yeah!')
    elif rec.intersects(C1) is False:
        print("No!")
    else :
        print('What?')
    print(rec.intersects(C1))

