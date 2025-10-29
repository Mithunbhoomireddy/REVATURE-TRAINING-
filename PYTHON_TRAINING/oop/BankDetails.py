class BankDetails:
    def __init__(self,cid,cname,bal):
        self.cid = cid
        self.cname = cname
        self.bal = bal

    def welcome_message(self):
        print("welcome to sbi")

    def display_bankDetails(self):
        print(f"cid:{self.cid} cname:{self.cname} balence:{self.bal}")
