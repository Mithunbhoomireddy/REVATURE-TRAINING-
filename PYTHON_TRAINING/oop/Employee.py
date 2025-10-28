class Employee:
    def __init__(self,empid,ename,bp):
        self.empid=empid
        self.empname=ename
        self.bp=bp

    def cal_allowence(self):
        return (self.bp*0.1)+(self.bp*0.05)

    def cal_ded(self):
        return self.bp*0.03

    def cal_grosspay(self):
        return self.bp+self.cal_allowence()

    def cal_netpay(self):
        return self.cal_grosspay()-self.cal_ded()
