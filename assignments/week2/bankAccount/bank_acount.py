class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
        else:
            print("Insufficient Funds")
        return self
    def display_account_info(self):
        print(f"Hello " + self.name, "your account balance is: $" + str(self.balance), ".")
        return self
    def yield_interest(self):
        self.balance = (self.balance * self.int_rate)
        return self
# I'd like to have the program read the users and return info rather than read a list.
@classmethod
def all_info(cls):
    for BankAccount in cls.BankAccount:
        BankAccount.display_account_info()

jay = BankAccount("Jay O'Meara", 1.25, 20000)
kym = BankAccount("Kym O'Meara", 1.1, 9853)

jay.display_account_info()
kym.display_account_info()

jay.deposit(2500).yield_interest()
kym.deposit(900).deposit(1800).withdraw(500).yield_interest().withdraw(1000000)


jay.display_account_info()
kym.display_account_info()


# BankAccount.all_info()