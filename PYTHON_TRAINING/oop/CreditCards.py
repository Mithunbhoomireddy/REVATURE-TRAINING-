from oop.BankDetails import BankDetails


class CreditCard(BankDetails):
    def __init__(self,cid,cname,bal,cscore,status):
        super().__init__(cid,cname,bal)
        self.cscore=cscore
        self.status=status

    def welcome_message(self):
        print("welcome to credit card:",self.cname)
    def display_credit_details(self):
        print(f"cscore:{self.cscore}  status:{self.status}")

