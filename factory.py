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
        Isside = float(input("What is the length of the two equal sides?"))
        Isbase = float(input("What is the length of the base?"))
        ITx = float(input("What is the x-coordinate of the centerpoint?"))
        ITy = float(input("What is the y-coordnate of the centerpoint?"))
        Isformula = input("Are you looking for the area or perimeter?").lower().strip()

        t2 = IsTriangle(Isbase, Isside, ITx, ITy, Isformula)
        if Isformula == "area":
            angleIs = cmath.acos((Isside**2+Isbase**2-Isside**2)/(2*Isside*Isbase))
            heightIs = cmath.sin(angleIs)* Isside
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
        Scy = float(input("What is the y-coordnate of the centerpoint?"))
        Scx = float(input("What is the x-coordinate of the centerpoint?"))
        Scside1 = float(input("What's the length of side 1?"))
        Scside2 = float(input("What's the length of side 2?"))
        Scside3 = float(input("What's the length of side 3?"))
        Scfunction = input("Are you looking for the area or perimeter?").strip().lower()

        t3= ScTriangle(Scx, Scy, Scside1, Scside2, Scside3, Scfunction)

        if Scfunction == "area":
            angleSc = cmath.acos((Scside1**2+Scside2**2-Scside3**2)/(2*Scside1*Scside2))
            heightSc = cmath.sin(angleSc)* Scside2
            areaSc= 1/2*Scside1*heightSc
            print("Area =", areaSc)
        elif Scfunction == "perimeter":
            perimeterSc = Scside1 + Scside2 + Scside3
            print("Perimeter =", perimeterSc)
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
    Eradius1 = float(input("What's the length of the longer radius?"))
    Eradius2 = float(input("What's the length of the shorter radius?"))
    Ex = float(input("What's the x-coordinate of the certerpoint?"))
    Ey = float(input("What's the y-coordinate of the centerpoint?"))
    Efunction = input("Are you trying to find the circumfrence or area?").lower().strip()
    if Efunction == "area":
        Earea= math.pi*Eradius1*Eradius2
        print("Area = approximately", Earea)
    elif Efunction == "circumfrence":
        Ecircumfrence = math.pi*(3*(Eradius1 + Eradius2) - math.sqrt((3*Eradius1 + Eradius2)*(Eradius1 + 3*Eradius2)))
        print("Circumfrence = approximately", Ecircumfrence)
    else:
        print("Error: Check spelling")

else:
    print("Error must be a valid shape- Check spelling.")