import math
import cmath
class Shape:
    def name(self):
        raise RuntimeError ("Error: Child class function not defined")
    def area(self): 
        raise RuntimeError ("Error: Child class function not defined")
    def perimeter(self):
        raise RuntimeError ("Error: Child class function not defined")

class ScTriangle(Shape):
        def __init__(self, Scx, Scy, Scside1, Scside2, Scside3):
            self.side1 = Scside1
            self.side2 = Scside2
            self.side3 = Scside3
            self.x = Scx
            self.y = Scy
        def name(self):
            return "Scalene Triangle"
        def area(self):
            heightSc = cmath.sin(angleSc)* self.side2
            angleSc = cmath.acos((self.side1**2+self.side2**2-self.side3**2)/(2*self.side1*self.side2))
            return 1/2*self.side1*heightSc
        def perimeter(self):
             return self.side1 + self.side2 + self.side3
        
class EqTriangle(Shape):
            def __init__(self, side, x, y):
                self.x = x
                self.y= y
                self.side = side
            def name(self):
                return "Equilateral Triangle"
            
class IsTriangle(Shape):
            def __init__(self, Isbase, Isside, ITx, ITy):
                self.base = Isbase
                self.side =Isside
                self.x = ITx
                self.y = ITy
            def name(self):
                return "Isosceles Triangle"


class Rectangle(Shape):
        def __init__(self, Rlength, Rheight, Rx, Ry):
            self.length = Rlength
            self.height = Rheight
            self.x = Rx
            self.y = Ry
        def name(self):
            return "Rectangle"
        def area(self):
            return self.length*self.height
        def perimeter(self):
            return self.length*2+self.height*2

class Circle(Shape):
        def __init__(self, radius, Cx, Cy):
            self.radius = radius
            self.Cx = Cx
            self.Cy = Cy
        def name(self):
            return "Circle"
        def area (self):
                return math.pi*self.radius**2
        def perimeter (self):
             return 2*math.pi*self.radius

class Ellipse(Shape):
        def __init__(self, Eradius1, Eradius2, Ex, Ey):
            self.Eradius1 = Eradius1
            self.Eradius2 = Eradius2
            self.Ex = Ex
            self.Ey = Ey
        def name(self):
            return "Ellipse"
        def area(self):
            return self.Eradius1*math.pi*self.Eradius2
        def perimeter(self):
             return math.pi*(3*(self.Eradius1 + self.Eradius2) - math.sqrt((3*self.Eradius1 + self.Eradius2)*(self.Eradius1 + 3*self.Eradius2)))




