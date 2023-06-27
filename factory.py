import cmath
import math
from classdef import *
shape = input("What shape would you like to make: triangle, rectangle, circle, or ellipse?").lower().strip()

if shape == "triangle": 
    typeT = input("What type of triangle: Equilateral, Isosceles, or Scalene?").lower().strip()
    if typeT == "equilateral":
        ETx = float(input("What's the x coordinate of the centerpoint?"))
        ETy = float(input("What's the y coordinate of the centerpoint?"))
        Eqside = float(input("What is the length of a side?"))
        Eqequation = input("Would you like to find the area or perimeter?").lower().strip()
        t1= EqTriangle(Eqside, ETx, ETy)
        if Eqequation == "area":
            print(t1.area())
        elif Eqequation == "perimeter":
            print(t1.perimeter())
        else:
            print("Invalid input, check spelling")

        EQname = t1.name()
        print(t1.name())

    elif typeT == "isosceles":
        Isside = float(input("What is the length of the two equal sides?"))
        Isbase = float(input("What is the length of the base?"))
        ITx = float(input("What is the x-coordinate of the centerpoint?"))
        ITy = float(input("What is the y-coordnate of the centerpoint?"))
        Isformula = input("Are you looking for the area or perimeter?").lower().strip()

        t2 = IsTriangle(Isbase, Isside, ITx, ITy)
        if Isformula == "area":
            print(t2.area())
        elif Isformula == "perimeter":
            print(t2.perimeter())
        else:
            print("Invalid input, check spelling")

        Isname= t2.name()
        print(t2.name())

    elif typeT == "scalene":
        Scy = float(input("What is the y-coordnate of the centerpoint?"))
        Scx = float(input("What is the x-coordinate of the centerpoint?"))
        Scside1 = float(input("What's the length of side 1?"))
        Scside2 = float(input("What's the length of side 2?"))
        Scside3 = float(input("What's the length of side 3?"))
        Scfunction = input("Are you looking for the area or perimeter?").strip().lower()

        t3= ScTriangle(Scx, Scy, Scside1, Scside2, Scside3)

        if Scfunction == "area":
            angleSc = cmath.acos((Scside1**2+Scside2**2-Scside3**2)/(2*Scside1*Scside2))
            heightSc = cmath.sin(angleSc)* Scside2
            print("Area =", t3.area())
        elif Scfunction == "perimeter":
            print("Perimeter =", t3.perimeter())
        else:
            print("Invalid input, check spelling")

        Scname = t3.name()
        print(t3.name())

    else:
        print("Must be a valid triangle- Check spelling.")

elif shape == "rectangle": 
    Rheight = float(input("What is the height of the rectangle?"))
    Rlength = float(input("What is the length of the rectangle?"))
    Rx = input("What is the x-coordinate of the centerpoint")
    Ry = input("What is the y-coordinate of the centerpoint?")
    Rfunction = input("Whould you like to find the area or perimeter?")

    R1 = Rectangle(Rlength, Rheight, Rx, Ry)

    if Rfunction == "perimeter":
      print(R1.perimeter())
    elif Rfunction == "area":
        print(R1.area())
    else:
        print("Invalid input, check spelling")

    name = R1.name()
    print(R1.name())

elif shape == "circle":
    radius = float(input("What's the radius of the circle?"))
    Cx= float(input("What is the x coordinate of the centerpoint?"))
    Cy= float(input("What is the y coordinate of the centerpoint?"))
    Cfunction = input("Would you like to find the circumfrence or area?")
    C1 = Circle(radius, Cx, Cy)
    if Cfunction == "circumfrence":
        print("Circumfrence =", C1.perimeter())
    elif Cfunction == "area":
        Carea = float(math.pi * radius**2)
        print("area =", Carea)
    else:
        print("Error: Check spelling. ")

elif shape == "ellipse":
    Eradius1 = float(input("What's the length of the longer radius?"))
    Eradius2 = float(input("What's the length of the shorter radius?"))
    Ex = float(input("What's the x-coordinate of the certerpoint?"))
    Ey = float(input("What's the y-coordinate of the centerpoint?"))
    Efunction = input("Are you trying to find the circumfrence or area?").lower().strip()
    E1 = Ellipse(Eradius1, Eradius2, Ex, Ey)
    if Efunction == "area":
        print("Area = approximately", E1.area())
    elif Efunction == "circumfrence":
        print("Circumfrence = approximately", E1.perimeter())
    else:
        print("Error: Check spelling")

else:
    print("Error must be a valid shape- Check spelling.")