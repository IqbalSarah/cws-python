class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"My name is {self.name} and my age is {self.age}"

    def display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")


s1 = Student("Anirudh", 55)
s2 = Student("Sagar", 15)
print(s1)
print(s2)
# s1.display()
