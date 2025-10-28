from oop.Employee import Employee

empid=int(input("enter employee id:"))
ename=input("enter employee name:")
bp=float(input("enter basic pay:"))

employee=Employee(empid,ename,bp)

print(f"Employee id:{employee.empid} \n Ename:{employee.ename} \n"
      f"Gross pay:{employee.cal_grosspay()} \n"
      f"Net pay:{employee.cal_netpay()}")