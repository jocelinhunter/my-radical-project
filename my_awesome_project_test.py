
from classdef import *
import math
import pytest
def test_rectangle():
    r1 = Rectangle(4,5,5,5)
    r1a= r1.area()
    assert r1a == 20
    r1p = r1.perimeter()
    assert r1p == 18

    r2 = Rectangle(6,7,8,8)
    r2a= r2.area()
    assert r2a == 42
    r2p = r2.perimeter()
    assert r2p == 26

def test_circle():
    c1 =  Circle(4,4,4)
    c1a= c1.area()
    assert c1a == math.pi*16
    c1p = c1.perimeter()
    assert c1p == math.pi*8

    c2 = Circle(8,4,4)
    c2a = c2.area()
    assert c2a == 64*math.pi
    c2p = c2.perimeter()
    assert c2p ==16*math.pi

def test_Striangle():
    t1 = ScTriangle(5,5,7,8,9)
    t1a = t1.area()
    assert t1a == pytest.approx(26.83281573)
    t2 = ScTriangle(5,5,6,5,4)
    t2a = t2.area()
    assert t2a == pytest.approx(9.921567418)

def test_Itriangle():
    t3 = IsTriangle(5,7,4,4)
    t3a = t3.area()
    assert t3a == pytest.approx(16.34587104)
    t4 = IsTriangle(6,4,3,3)
    t4a = t4.area()
    assert t4a == pytest.approx(7.937253933)

def test_Etriangle():
    t5 = EqTriangle(4,5,5)
    t5a = t5.area()
    assert t5a == pytest.approx(6.92820323)
    t6 = EqTriangle(8,9,2)
    t6a = t6.area()
    assert t6a == pytest.approx(27.71281292)

def test_ellipse():
    e1 = Ellipse(5,8,5,5)
    e1a = e1.area()
    assert e1a == pytest.approx(125.66371)
    e2 = Ellipse(7,4,6,9)
    e2a = e2.area()
    assert e2a == pytest.approx(87.96459)