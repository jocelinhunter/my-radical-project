import pyCAPS
from factory import *

#loading in file
if shape == "rectangle":
    filename = "square1.csm"
    print("Loading contents of file", filename)
    capsProblem = pyCAPS.Problem(problemName = "design_rect", capsFile = filename, outLevel = 0)
    square = capsProblem.geometry

    square.despmtr["xcenter"].value = Rx
    square.despmtr["ycenter"].value = Ry
    square.despmtr["zcenter"].value = 0
    square.despmtr["xlen"].value = Rlength
    square.despmtr["ylen"].value = Rheight
    square.despmtr["zlen"].value = 0


#ability to see the build
    print("Building and viewing geometry")
    capsProblem.geometry.view() 

if shape == "triangle":
    if typeT == "equilateral":
        filename = "EqTri.csm"
        print("Loading contents of file", filename)
        capsProblem = pyCAPS.Problem(problemName = "design_eqt",capsFile = filename, outLevel = 1)
        EqTri = capsProblem.geometry
        x_cent = ETx #give function name
        y_cent = ETy
        length = Eqside
        EqTri.despmtr["xcent"].value = x_cent
        EqTri.despmtr["ycent"].value = y_cent
        EqTri.despmtr["zcent"].value = 0
        EqTri.despmtr["length"].value = length
        print("Building and viewing geometry")
        capsProblem.geometry.view()

    if typeT == "isosceles":
        filename = "IsTri.csm"
        print("Loading contents of file", filename)
        capsProblem = pyCAPS.Problem(problemName = "design_Ist", capsFile = filename, outLevel = 1)
        IsTri = capsProblem.geometry
        x_cent = ITy
        y_cent = ITx
        z_cent = 0
        side = Isside
        base = Isbase
        IsTri.despmtr["xstart"].value = x_cent
        IsTri.despmtr["ystart"].value = y_cent
        IsTri.despmtr["zstart"].value = z_cent
        IsTri.despmtr["s"].value = side
        IsTri.despmtr["b"].value = base
        print("Building and viewing geometry")
        capsProblem.geometry.view()

    if typeT == "scalene":
        filename = "ScTri.csm"
        print("Loading contents of file", filename)
        capsProblem = pyCAPS.Problem(problemName = "design_Sct", capsFile = filename, outLevel = 1)
        ScTri = capsProblem.geometry
        s1 = Scside1
        s2 = Scside2
        s3 = Scside3



        print("Loading geometry...")
        capsProblem.geomtery.view()


if shape == "circle":
    filename = "Circ.csm"
    print("Loading contents of file", filename)
    capsProblem = pyCAPS.Problem(problemName = "design_Circ", capsFile = filename, outLevel = 1)
    Circ = capsProblem.geometry
    xcent = Cx
    ycent = Cy
    radius = Cradius
    Circ.despmtr["radius1"].value = radius
    Circ.despmtr["xcent"].value = xcent
    Circ.despmtr["ycent"].value = ycent
    print("Loading Geometry...")
    capsProblem.geometry.view()

if shape == "ellipse":
    filename = "Ell.csm"
    print("loading contents of file", filename)
    capsProblem = pyCAPS.Problem(problemName = "design_Ell", capsFile = filename, outLevel = 1)
    Ell = capsProblem.geometry
    xcent = Ex
    ycent = Ey
    radius1 = Eradius1
    radius2 = Eradius2
    Ell.despmtr["radius1"].value = radius1
    Ell.despmtr["radius2"].value = radius2
    Ell.despmtr["xcent"].value = xcent
    Ell.despmtr["ycent"].value = ycent

    print("Loading geometry")
    capsProblem.geometry.view()