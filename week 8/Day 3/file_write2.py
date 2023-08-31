"""
Ask name,age,gender from user.

Filename = anirudh khurana.txt
My name is {}
My gender is {}
My age is {}
"""


def writeIntoFile(name, age, gender):
    f = open(f"{name}.txt", "w")
    f.write(f"My name is {name}\n")
    f.write(f"My age is {age}\n")
    f.write(f"My gender is {gender}\n")
    f.close()


name = input("Enter name = ")
age = int(input("Enter age = "))
gender = input("Enter gender = ")
writeIntoFile(name, age, gender)
