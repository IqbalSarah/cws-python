from random import randint


class Bank:
    def __init__(self):
        self.accountNumber = randint(100000, 999999)
        self.name = input("Enter your account name = ")
        self.balance = 0
        self.branch = input("Enter branch name = ")

    def display(self):
        print(f"Account number = {self.accountNumber}")
        print(f"Account name = {self.name}")
        print(f"Account balance = {self.balance}")
        print(f"Account branch = {self.branch}")

    def showBalance(self):
        print(f"Your current balance is = {self.balance}")

    def withdraw(self):
        amt = int(input("Enter amount to withdraw = "))
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amt
            self.showBalance()

    def deposit(self):
        amt = int(input("Enter amount to deposit = "))
        self.balance += amt
        self.showBalance()


b1 = Bank()
b2 = Bank()

b1.withdraw()
b1.deposit()
b1.display()
b2.display()
