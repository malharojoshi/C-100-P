class ATM(object):
    def _init_(self,atm_card_number,pin_number):
        self.atm_card_number=atm_card_number
        self.pin_number=pin_number
    def cashWithdrawl(self):
        print("500")
    def BalanceEnquiry(self):
        print("200000")
Joe= ATM("9846","887354","Audi",100)
print(Joe.atm_card_number)