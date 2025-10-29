from oop.College import College

class Teacher_Details(College):
    def __init__(self,ccode,cname,empid,tname,dept):
        College.__init__(self,ccode,cname)
        self._empid = empid
        self._tname= tname
        self._dept = dept

    def display(self):
        print(f"{self._ccode} \t {self._cname}\n"
              f"{self._empid} \n {self._tname}\n {self._dept}")


