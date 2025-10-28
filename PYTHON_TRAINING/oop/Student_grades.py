from math import expm1

from oop.StuExCurr import StuExCurr

rollno=int(input("Enter roll no:"))
sname=input("Enter student name:")
n1=int(input("Enter student mark1:"))
n2=int(input("Enter student mark2:"))
n3=int(input("Enter student mark3:"))
ccode=int(input("Enter course code:"))
cname=input("Enter course name:")
exm1=int(input("Enter exercise mark1:"))
exm2=int(input("Enter exercise mark2:"))
exm3=int(input("Enter exercise mark3:"))

# stu=Student_Details(ccode,cname,rollno,sname,n1,n2,n3)
# print(f"rollno:{stu.get_rollno}\nsname: {stu.get_sname()}\nmark1: {stu.get_n1()}\nmark2: {stu.get_n2()}\nmark3: {stu.get_n3()}\n"
#       f"total:{stu.cal_tot()}\naverage:{stu.calc_avg()}")
# print(stu.display()[0],f"\n{stu.display()[1]}")

stu=StuExCurr(ccode,cname,rollno,sname,n1,n2,n3,exm1,exm2,exm3)
print(f"rollno:{stu.get_rollno}\nsname: {stu.get_sname()}\nmark1: {stu.get_n1()}\nmark2: {stu.get_n2()}\nmark3: {stu.get_n3()}\n"
      f"total:{stu.cal_tot()}\naverage:{stu.calc_avg()}")
print(f"collegecode:{stu.display()[0]}\ncollegename:{stu.display()[1]}")
print(f"extra circular exam marks total:{stu.calc_exm()}")