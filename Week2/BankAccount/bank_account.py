class BankAccount:
    
    bank_name = "First National Dojo"

    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self
        
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

account1 = BankAccount(0.05, 200)
account2 = BankAccount(0.04, 100)
account1.deposit(50).deposit(20.05).deposit(400.56).withdraw(204.10).yield_interest().display_account_info()
account2.deposit(100).deposit(75).withdraw(275).withdraw(10).withdraw(35).withdraw(42).yield_interest().display_account_info()