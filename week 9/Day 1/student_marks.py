"""
Create a class Student

Create method setData and ask for name,phy,sci,eng,hind,math
Create method display and display all details
Create method totalMarks and display total marks (total - local variable)
Create method totalMarks2 and return total marks (total - local variable)
Create method updateName, enter your new name, then call display()
"""


class Student:
    def setdata(self):
        self.name = input("Enter your name : ")
        self.phy = int(input("Enter physics marks : "))
        self.sci = int(input("Enter science marks = "))
        self.eng = int(input("Enter english marks = "))
        self.hindi = int(input("Enter hindi marks = "))
        self.maths = int(input("Enter maths marks = "))

    def display(self):
        print(f"My name is {self.name}")
        print(f"My physics marks is {self.phy}")
        print(f"My science marks is {self.sci}")
        print(f"My english marks is {self.eng}")
        print(f"My hindi marks is {self.hindi}")
        print(f"My maths marks is {self.maths}")

    def totalmarks(self):
        total = self.phy + self.sci + self.eng + self.hindi + self.maths
        print(f"My total marks is {total}")

    def totalmarks2(self):
        total = self.phy + self.sci + self.eng + self.hindi + self.maths
        return total

    def updateName(self):
        self.name = input("Enter your new name : ")


s1 = Student()

s1.setdata()
s1.display()
s1.totalmarks()
print(s1.totalmarks2())
s1.updateName()
s1.display()
