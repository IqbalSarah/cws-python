class Student:
    # Dunder
    def __init__(self):  # Constructor (Memory Initialize)
        self.name = input("Enter student name =")
        self.age = int(input("Enter student age ="))
        self.gender = input("Enter student gender =")
        self.phone = int(input("Enter student phone ="))

    def display(self):
        print(f"Name = {self.name}, age = {self.age}, gender= {self.gender}")


s1 = Student()
s2 = Student()
s1.display()
s2.display()
