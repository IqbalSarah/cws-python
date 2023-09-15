"""
Make a class Employee

Class variable should be asked from user
They should be name, age, gender, department, experience,role
Employee ID should be generated automatically and should
be ALNUM(8 characters) - TH78AC65, 8909JH76

Methods
displayBasis() = Print details about emp_id, name,age,gender
displayinfo() = Print department,exp, role
changeDepartment() = Ask new department, and replace
changeExp() = Ask new experience, and replace
changeRole() = Ask new  role, and replace
"""

import random, string


def generateRandomID():
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(8)
    )


class Employee:
    def __init__(self):
        self.employeeId = generateRandomID()
        self.name = input("Enter your name = ")
        self.age = input("Enter your age = ")
        self.gender = input("Enter your gender = ")
        self.department = input("Enter your department = ")
        self.experience = input("Enter your experience = ")
        self.role = input("Enter your role = ")

    def displayBasic(self):
        print(f"Employee ID : {self.employeeId}")
        print(f"Nmae : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")

    def displayInfo(self):
        print(f"Department : {self.department}")
        print(f"Experience : {self.experience}")
        print(f"Role : {self.role}")

    def changeDepartment(self):
        self.department = input("Enter new department = ")

    def changeExp(self):
        self.experience = input("enter new experience = ")

    def changerole(self):
        self.role = input("Enter your new role = ")


e1 = Employee()
e1.displayBasic()
e1.displayInfo()
e1.changeDepartment()
e1.changeExp()
e1.changerole()
e1.displayBasic()
e1.displayInfo()
