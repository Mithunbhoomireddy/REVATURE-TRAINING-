from StuExCurr import StuExCurr
from Teacher_Details import Teacher_Details

class Final_Eval(StuExCurr,Teacher_Details):
    def __init__(self,ccode,cname,rollno,sname,n1,n2,n3,exm1,exm2,exm3,empid,tname,dept,
                 feedback_From_Teacher):
        StuExCurr.__init__(self,ccode,cname,rollno,sname,n1,n2,n3,exm1,exm2,exm3)
        Teacher_Details.__init__(self,ccode,cname,empid,tname,dept)
        self.feedback_From_Teacher = feedback_From_Teacher

