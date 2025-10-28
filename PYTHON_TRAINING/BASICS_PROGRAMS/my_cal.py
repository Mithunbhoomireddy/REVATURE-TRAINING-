"""
my calculations
"""
from mypackage.shape_calculations import (area_of_circle,area_of_square,area_of_rectangle,
                                          circumference_of_circle,perimeter_of_square,
                                          perimeter_of_rectangle)

cir_radius=float(input("enter the radius of the circle:"))
sq_side=float(input("enter the side of the squre:"))
rec_len=float(input("enter the length of the rectangle:"))
rec_width=float(input("enter the width of the rectangle:"))

print(f"area of circle is: {area_of_circle(cir_radius)}")
print(f"circumstance of circle is: {circumference_of_circle(cir_radius)}")
print(f"area of square is: {area_of_square(sq_side)}")
print(f"perimeter of square is: {perimeter_of_square(sq_side)}")
print(f"area of square is: {area_of_rectangle(rec_len,rec_width)}")
print(f"perimeter of rectangle is: {perimeter_of_rectangle(rec_len,rec_width)}")
