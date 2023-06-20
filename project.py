import cmath
import math
class Shape:
    def name(self):
        raise RuntimeError ("Error: Child class function not defined")

shape = input("What shape would you like to make: triangle, rectangle, circle, or ellipse?").lower().strip()

if shape == "triangle": 
    typeT = input("What type of triangle: Equilateral, Isosceles, or Scalene?").lower().strip()
if typeT == "equilateral":
    class EqTriangle(Shape):
        def __init__(self, side, x, y, Eqequation):
            self.x = x
            self.y= y
            self.side = side
            self.equation = Eqequation
        def name(self):
            return "Equilateral Triangle"

    ETx = float(input("What's the x coordinate of the centerpoint?"))
    ETy = float(input("What's the y coordinate of the centerpoint?"))
    Eqside = float(input("What is the length of a side?"))
    Eqequation = input("Would you like to find the area or perimeter?").lower().strip()

    t1= EqTriangle(Eqside, ETx, ETy, Eqequation)
    if Eqequation =="area":
        areaET = print("area =", 1/2* Eqside *cmath.sin(math.pi/3)*Eqside)
        print(areaET)
    elif Eqequation == "perimeter":
        perimeterET = Eqside*3
        print(perimeterET)
    else:
        print("Invalid input, check spelling")

    EQname = t1.name()
    print(t1.name())


elif typeT == "isosceles": 
    class IsTriangle(Shape):
        def __init__(self, Isbase, Isside, ITx, ITy, Isformula):
            self.base = Isbase
            self.side =Isside
            self.x = ITx
            self.y = ITy
            self.formula = Isformula
        def name(self):
            return "Isosceles Triangle"
    

    Isbase = float(input("What is the length of the base?"))
    Isside = float(input("What is the length of the side?"))
    ITx = float(input("What is the x-coordinate of the centerpoint?"))
    ITy = float(input("What is the y-coordnate of the centerpoint?"))
    Isformula = input("Are you looking for the area or perimeter?").lower().strip()

    t2 = IsTriangle(Isbase, Isside, ITx, ITy)
    if Isformula == "area":
        angleIs = int(cmath.acos*(Isbase**72/2*Isside*Isbase)) #HOW TO DO EXPONENT
        heightIs = int(cmath.sin(angleIs)* Isside)
        ISarea = 1/2* Isbase * heightIs
        print(ISarea)
    elif Isformula == "perimeter":
        ISperimeter = 2*Isside+Isbase
        print(ISperimeter)
    else:
        print("Invalid input, check spelling")

    Isname= t2.name()
    print(t2.name())


elif typeT == "scalene":
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

    Scy = float(input("What is the y-coordnate of the centerpoint?"))
    Scx = float(input("What is the x-coordinate of the centerpoint?"))
    Scside1 = float(input("What's the length of side 1?"))
    Scside2 = float(input("What's the length of side 2?"))
    Scside3 = float(input("What's the length of side 3?"))
    Scfunction = input("Are you looking for the area or perimeter?").strip().lower()

    t3= ScTriangle(Scx, Scy, Scside1, Scside2, Scside3)

    if Scfunction == "area":
        angleSc = int(cmath.acos(Scside1**2+Scside2**2-Scside3**2*1/2*Scside1*Scside2))
        heightSc = int(cmath.sin(angleSc)* Scside1)
        areaSc= int(1/2*Scside1*heightSc)
        print("Area =", areaSc)
    elif Scfunction == "perimeter":
        perimeterSc = int(Scside1 + Scside2 + Scside3)
        print("Perimeter =", perimeterSc)
    else:
        print("Invalid input, check spelling")

    Scname = t3.name()
    print(t3.name())

else:
        print("Error: Check spelling.")


if shape == "rectangle": 
    class Rectangle(Shape):
        def __init__(self, Rlength, Rheight, Rx, Ry, Rfunction):
            self.length = Rlength
            self.height = Rheight
            self.x = Rx
            self.y = Ry
            self.function = Rfunction
        def name(self):
            return "Rectangle"

    Rheight = float(input("What is the height of the square?"))
    Rlength = float(input("What is the length of the square?"))
    Rx = input("What is the x-coordinate of the centerpoint")
    Ry = input("What is the y-coordinate of the centerpoint?")
    Rfunction = ("Whould you like to find the area or perimeter?")

    Rname = Rectangle(Rlength, Rheight, Rx, Ry, Rfunction)

    if Rfunction == "perimeter":
        Rperimeter = float(Rlength*2 + Rheight*2)
        print("perimeter =", Rperimeter)    
    elif Rfunction == "area":
        Rarea = float(Rheight * Rlength)
        print("area = ", Rarea)
    else:
        print("Invalid input, check spelling")

    name = Rname.name()
    print(Rname.name())

elif shape == "circle":
    class Circle(Shape):
        def __init__(self, radius, Cx, Cy, Cfunction):
            self.radius = radius
            self.Cx = Cx
            self.Cy = Cy
            self.function = Cfunction
        def name(self):
            return "Circle"
        
    Cradius = float(input("What's the radius of the circle?"))
    Cfunction = input("Would you like to find the circumfrence or area?")
    if Cfunction == "circumfrence":
        Cperimeter = float(2*math.pi* Cradius)
        print("Circumfrence =", Cperimeter)
    elif Cfunction == "area":
        Carea = float(math.pi * Cradius**2)
        print("area =", Carea)
    else:
        print("Error: Check spelling. ")

elif shape == "ellipse":
    class Ellipse(Shape):
        def __init__(self, Eradius1, Eradius2, Ex, Ey, Efunction):
            self.Eradius1 = Eradius1
            self.Erasius1 = Eradius2
            self.Ex = Ex
            self.Ey = Ey
            self.Efunction = Efunction
        def name(self):
            return "Ellipse"
        
    Eradius1 = float(input("What's the length of the horizontal radius?"))
    Eradius2 = float(input("What's the length of the vertical radius?"))
    Ex = float(input("What's the x-coordinate of the certerpoint?"))
    Ey = float(input("What's the y-coordinate of the centerpoint?"))
    Efunction = input("Are you trying to find the circumfrence or area?").lower().strip()
    if Efunction == "area":
        Earea= float(...)
        print("Area =", Earea)
    elif Efunction == "circumfrence":
        Ecircumfrence = math.pi*(3*(Eradius1 + Eradius2) - math.sqrt((3*Eradius1 + Eradius2)*(Eradius1 + 3*Eradius2)))
        print("Circumfrence = approximately", Ecircumfrence)
    else:
        print("Error: Check spelling")

else:
    print("Error: Check spelling")