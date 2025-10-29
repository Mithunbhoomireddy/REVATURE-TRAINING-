from oop.College import College


class Student_Details(College):
    def __init__(self,ccode,cname,rollno,sname,n1,n2,n3):
        College.__init__(self,ccode,cname)
        self.__rollno=rollno
        self.__sname=sname
        self.__n1=n1
        self.__n2=n2
        self.__n3=n3

    @property
    def get_rollno(self):
        return self.__rollno

    @get_rollno.setter
    def set_rollno(self,rollno):
        self.__rollno=rollno

    def get_sname(self):
        return self.__sname

    def set_sname(self,sname):
        self.__sname=sname

    def get_n1(self):
        return self.__n1

    def set_n1(self,n1):
        self.__n1=n1

    def get_n2(self):
        return self.__n2

    def set_n2(self,n2):
        self.__n2=n2

    def get_n3(self):
        return self.__n3

    def set_n3(self,n3):
        self.__n3=n3

    def cal_tot(self):
        return self.__n1+self.__n2+self.__n3

    def calc_avg(self):
        return self.cal_tot()/3
