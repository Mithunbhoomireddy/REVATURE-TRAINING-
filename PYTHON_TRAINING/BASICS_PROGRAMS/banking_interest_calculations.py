"""
banking interest calculations
"""
from mypackage.interest_calculations import simple_interest,compound_interest
prin=float(input("enter principal amount:"))
ny=float(input("enter number of years:"))
roi=float(input("enter roi amount:"))
t=float(input("enter time:"))
si,amt=simple_interest(prin=prin,ny=ny,roi=roi)
print(f"simple interest : {si} and amount : {amt}")
ci,amt=compound_interest(prin=prin,t=t,roi=roi)
print(f"compound interest : {ci} and amount : {amt}")
