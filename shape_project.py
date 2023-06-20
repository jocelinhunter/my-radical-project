#i realize that the questions will probably have to be changed to work with other platforms

import math

class Shape: 
    def name():
        raise RuntimeError ("Error: Child class function not defined")


    class EqTriangle: #equilateral vs isoscelese vs scalene
       def __init__(self, side, x, y):
            self.side = side
            self.y= y
            self.x = x 

            
t1 = EqTriangle(4, 5, 7)
print(t1.side)




    class Ellipse:
        def __init__(self):
            a = float(input("What's a?"))
            b = float(input("What's b?"))
            permieterE = math.pi[ 3*(a + b)] - math.sqrt*(3a + b)*(a + 3b)
            areaE = (math.pi * a * b)
            print(int(areaE))





    class Circle:
        def __init__(self):
            r = float(input("What's the radius?"))
            perimeterC = 2 * math.pi * r
            areaC = (math.pi * r * r)
            if Shape.formula == "area":
                print(areaC)





    class Rectangle:
        def __init__(self): 
            l = (input("What's the length of the rectangle?"))
            w =(input("whats the width of the rectangle?"))
            perimeterR = 2*l + 2*w
            areaR = l * w
            print(float(areaR))
if Shape.shapes == "rectangle" or "square":
        print()




input(Shape.shape)
if Shape.shape in Shape.shapes != ["rectangle", "triangle", "ellipse", "circle"]:
        print("Shape must be a rectangle, triangle, ellipse, or circle")