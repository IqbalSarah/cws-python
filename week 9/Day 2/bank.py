from random import randint


class Bank:
    def createAccount(self):
        self.accountNumber = randint(100000, 999999)
        self.name = input("Enter your account name = ")
        self.balance = 0
        self.branch = input("Enter branch name = ")

    # OR this function can also be used
    def createAccount2(self, name: str, branch: str = "City Light", balance: int = 0):
        self.accountNumber = randint(100000, 999999)
        self.name = name
        self.balance = balance
        self.branch = branch

    def display(self):
        print(f"Account number = {self.accountNumber}")
        print(f"Account name = {self.name}")
        print(f"Account balance = {self.balance}")
        print(f"Account branch = {self.branch}")


b1 = Bank()

b1.createAccount()
b1.display()
b1.createAccount2(name="Anirudh")
b1.display()
