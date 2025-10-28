from Student_Details import Student_Details

class StuExCurr(Student_Details):
    def __init__(self,ccode,cname,rollno,sname,n1,n2,n3,exm1,exm2,exm3):
        super().__init__(ccode,cname,rollno,sname,n1,n2,n3)
        self.exm1=exm1
        self.exm2=exm2
        self.exm3=exm3

    def calc_exm(self):
        return (self.exm1+self.exm2+self.exm3)
