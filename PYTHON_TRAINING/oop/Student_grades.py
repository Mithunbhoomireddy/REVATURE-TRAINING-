from math import expm1

from oop.Final_Eval import Final_Eval
from oop.StuExCurr import StuExCurr
from oop.Teacher_Details import Teacher_Details

rollno=int(input("Enter roll no:"))
sname=input("Enter student name:")
n1=int(input("Enter student mark1:"))
n2=int(input("Enter student mark2:"))
n3=int(input("Enter student mark3:"))
ccode=int(input("Enter course code:"))
cname=input("Enter course name:")
tname=input("Enter teacher name:")
empid=int(input("Enter employee id:"))
dept=input("Enter department:")
exm1=int(input("Enter exercise mark1:"))
exm2=int(input("Enter exercise mark2:"))
exm3=int(input("Enter exercise mark3:"))
feedback_From_Teacher=input("Enter feedback From Teacher:")

# stu=Student_Details(ccode,cname,rollno,sname,n1,n2,n3)
# print(f"rollno:{stu.get_rollno}\nsname: {stu.get_sname()}\nmark1: {stu.get_n1()}\nmark2: {stu.get_n2()}\nmark3: {stu.get_n3()}\n"
#       f"total:{stu.cal_tot()}\naverage:{stu.calc_avg()}")
# print(stu.display()[0],f"\n{stu.display()[1]}")

# stu=StuExCurr(ccode,cname,rollno,sname,n1,n2,n3,exm1,exm2,exm3)
# print(f"rollno:{stu.get_rollno}\nsname: {stu.get_sname()}\nmark1: {stu.get_n1()}\nmark2: {stu.get_n2()}\nmark3: {stu.get_n3()}\n"
#       f"total:{stu.cal_tot()}\naverage:{stu.calc_avg()}")
# print(f"collegecode:{stu.display()[0]}\ncollegename:{stu.display()[1]}")
# print(f"extra circular exam marks total:{stu.calc_exm()}")

# teacher=Teacher_Details(ccode,cname,empid,tname,dept)
# teacher.display()
final_eval=Final_Eval(ccode,cname,rollno,sname,n1,n2,n3,exm1,exm2,exm3,empid,tname,dept,
                 feedback_From_Teacher)
print(f"{final_eval.display()}\n"
      # f"{final_eval.display()[0]} \t {final_eval.display()[1]} \n"
      f"rollno:{final_eval.get_rollno}\nsname: {final_eval.get_sname()}\n"
      f"total:{final_eval.cal_tot()}\n"
      f"average:{final_eval.calc_avg()}"
      f"{final_eval.display()}")
