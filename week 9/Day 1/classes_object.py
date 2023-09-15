class Student:
    name = ""
    age = 0
    gender = ""


s1 = Student()
s2 = Student()

s1.name = "Sarah"
s1.age = 99
s1.gender = "Female"

print(f"s1 name = {s1.name}")
print(f"s1 age = {s1.age}")
print(f"s1 gender = {s1.gender}")

s2.name = "Ram"
s2.age = 20
s2.gender = "Male"

print(f"s2 name = {s2.name}")
print(f"s2 age = {s2.age}")
print(f"s2 gender = {s2.gender}")


# Shorten it


class Student:
    # Member/Class variables
    name = ""
    age = 0
    gender = ""

    def display(self):  # Methods
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")


s1 = Student()
s2 = Student()

s1.name = "Sarah"
s1.age = 99
s1.gender = "Female"

s2.name = "Ram"
s2.age = 20
s2.gender = "Male"

s1.display()
s2.display()


# More shortened


class Student:
    def setdata(self):
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age : "))
        self.gender = input("Enter your gender : ")

    def display(self):  # Methods
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My gender is {self.gender}")


s1 = Student()
s2 = Student()

s1.setdata()
s2.setdata()
s1.display()
s2.display()
