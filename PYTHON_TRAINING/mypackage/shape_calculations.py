"""
Area & circumstance of squre,circle,rectangle,
"""
from math import pi

def area_of_square(side):
    return side*side

def perimeter_of_square(side):
    return 4*side

def area_of_rectangle(length,width):
    return length*width

def perimeter_of_rectangle(length,width):
    return 2*(length+width)

def area_of_circle(radius):
    return pi * radius * radius

def circumference_of_circle(radius):
    return 2*pi*radius
