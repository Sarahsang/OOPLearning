class SavingsAccount:
    def __init__(self,accnum, accname, bal, irate):
        self.accnum = accnum
        self.accname = accname
        self.bal = bal
        self.irate = irate
    
    def deposit(self, amount):
        self.bal += amount
        
    def withdraw(self, amount):
        self.bal -= amount
        
    def calc_interest(self):
        self.bal += self.bal * self.irate
        
    
                
acct1 = SavingsAccount(123, 'John', 1000, 0.05)

