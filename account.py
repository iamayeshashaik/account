class Account:
    
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def deposit(self, amount):
        self.amount = amount
        self.dep = self.balance + self.amount
        return

    def withdrawl(self,W_amount):
        self.w_amount = W_amount
        self.wd = self.dep - self.w_amount
        return

    def getBalance(self):
        self.bal = self.balance + self.amount - self.w_amount
        return 

class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        self.interestRate = interestRate
        super().__init__(title ,balance)

    def deposit(self):
        super().deposit(amount=2000)
    def withdrawl(self):
        super().withdrawl(W_amount=500)
    def getBalance(self):
        super().getBalance()
        return
    def interestamount(self, intrst_amount):
        self.intrst_amount = intrst_amount 
        return
    def display(self):
        self.intrst_amount = self.bal / 100 * self.interestRate
        print(f"Name of Account Holder : {self.title} \nAfter deposit amount : {self.dep} \nAfter Withdrawl amount : {self.wd} \nAcc Balance : {self.bal} \nInterest : {self.interestRate} \nInterest_amount : {self.intrst_amount}")
        
obj = SavingsAccount("arun", 7000, 5)
print("\nChallenge-5 Output:- ")
obj.deposit()
obj.withdrawl()
obj.getBalance()
obj.display()