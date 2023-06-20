class Shape: 
    def name(self):
        raise RuntimeError ("Error: Child class function not defined")


class EqTriangle(Shape): #equilateral vs isoscelese vs scalene
    def __init__(self, side, x, y):
        self.side = side
        self.y= y
        self.x = x
    def name(self):
        return "Equilateral Triangle"


side = float(input("What's the side?")) 
x = float(input("What's the centerpoint's x value?"))
y = float(input("What's the centerpoint's y value?"))


t1 = EqTriangle(side, x, y)
print(t1.side)
name1= t1.name()
print(name1)

class IsTriangle(Shape):
    def __init__(self, side1, side2, x, y):
        self.side1 = side1
        self.side2 = side2 
        self.x = x
        self.y = y
    def name(self):
        return "Isosceles Triangle"

side1 = float(input("What's side 1?"))
side2 = float(input("What's side 2?"))
x = float(input("What's the centerpoint's x value?"))
y = float(input("What's the centerpoint's y value?"))

t2 = IsTriangle(side1, side2, x, y)
print(t2.side1)
name2 = t2.name()
print(t2.name())
