class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "checking" : BankAccount(.02,1000),
            "savings" : BankAccount(.05,2500)
        }
    def display_user_balance(self):
        print(f"Hello " + self.name, "your Checking balance is: $",str(self.account["checking"].display_account_info())+", and Savings balance is $", self.account['savings'].display_account_info())
        return self

class BankAccount: 
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def yield_interest(self):   
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self 
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
        else:
            print("Insufficient Funds")
        return self
    def display_account_info(self):
        return f"{self.balance}"


jay = User("Jay O'Meara", "jay@idlewild.industries")
kym = User("Kym O'Meara", "kym@idlewild.industries")

jay.display_user_balance()
kym.display_user_balance()

jay.account['checking'].deposit(2500)
kym.account['savings'].deposit(900).deposit(1800).withdraw(500).yield_interest().withdraw(1000000)


jay.display_user_balance()
kym.display_user_balance()
