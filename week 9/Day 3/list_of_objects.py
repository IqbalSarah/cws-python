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


accounts: list[Bank] = []

while True:
    print("\n1) Add an account")
    print("2) View all accounts")
    print("3) Search an account by account number")
    print("4) Deposit into your account")
    print("5) Withdraw from your account")
    print("6) Transfer money")
    print("7) Exit")
    choice = int(input("Enter your choice =  "))
    if choice == 1:
        obj = Bank()
        accounts.append(obj)
        # accounts.insert(0, obj)
    elif choice == 2:
        if len(accounts) == 0:
            print("No accounts added till yet.")
        else:
            for i in range(0, len(accounts)):
                accounts[i].display()
    elif choice == 3:
        acc_no = int(input("Enter account number = "))
        for i in range(len(accounts)):
            if accounts[i].accountNumber == acc_no:
                accounts[i].display()
                break
            else:
                print("No accounts found")
    elif choice == 4:
        acc_no = int(input("Enter account number = "))
        for i in range(len(accounts)):
            if accounts[i].accountNumber == acc_no:
                accounts[i].deposit()
                break
            else:
                print("Account not found")
    elif choice == 5:
        acc_no = int(input("Enter account number = "))
        for i in range(len(accounts)):
            if accounts[i].accountNumber == acc_no:
                accounts[i].withdraw()
                break
            else:
                print("Account not found")
    elif choice == 6:
        from_acc_no = int(input("Enter account number to send money from = "))
        for i in range(len(accounts)):
            if accounts[i].accountNumber == from_acc_no:
                to_acc_no = int(input("Enter account number to send money from = "))
                for j in range(len(accounts)):
                    if accounts[i].accountNumber == to_acc_no:
                        amt = int(input("Enter amount to transfer = "))
                        if accounts[i].balance < amt:
                            print("Insufficient balance")
                        else:
                            accounts[i] -= amt
                            accounts[j] += amt
                        break
                else:
                    print("No to-account found!")
                break
        else:
            print("No from-account found!")

    elif choice == 7:
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
