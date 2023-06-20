
class Shape:
    def name(self):
        raise RuntimeError ("Error: Child class function not defined")
    
class ScTriangle(Shape):
        def __init__(self, Scx, Scy, Scside1, Scside2, Scside3, Scfunction):
            self.side1 = Scside1
            self.side2 = Scside2
            self.side3 = Scside3
            self.x = Scx
            self.y = Scy
            self.function = Scfunction 
        def name(self):
            return "Scalene Triangle"
        
class EqTriangle(Shape):
            def __init__(self, side, x, y, Eqequation):
                self.x = x
                self.y= y
                self.side = side
                self.equation = Eqequation
            def name(self):
                return "Equilateral Triangle"
            
class IsTriangle(Shape):
            def __init__(self, Isbase, Isside, ITx, ITy, Isformula):
                self.base = Isbase
                self.side =Isside
                self.x = ITx
                self.y = ITy
                self.formula = Isformula
            def name(self):
                return "Isosceles Triangle"

class ScTriangle(Shape):
            def __init__(self, Scx, Scy, Scside1, Scside2, Scside3, Scfunction):
                self.side1 = Scside1
                self.side2 = Scside2
                self.side3 = Scside3
                self.x = Scx
                self.y = Scy
                self.function = Scfunction 
            def name(self):
                return "Scalene Triangle"

class Rectangle(Shape):
        def __init__(self, Rlength, Rheight, Rx, Ry, Rfunction):
            self.length = Rlength
            self.height = Rheight
            self.x = Rx
            self.y = Ry
            self.function = Rfunction
        def name(self):
            return "Rectangle"

class Circle(Shape):
        def __init__(self, radius, Cx, Cy, Cfunction):
            self.radius = radius
            self.Cx = Cx
            self.Cy = Cy
            self.function = Cfunction
        def name(self):
            return "Circle"

class Ellipse(Shape):
        def __init__(self, Eradius1, Eradius2, Ex, Ey, Efunction):
            self.Eradius1 = Eradius1
            self.Erasius1 = Eradius2
            self.Ex = Ex
            self.Ey = Ey
            self.Efunction = Efunction
        def name(self):
            return "Ellipse"






