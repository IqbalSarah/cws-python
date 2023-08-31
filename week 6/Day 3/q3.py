student = {}

number_of_students = int(input("Enter number of students = "))
for _ in range(0, number_of_students):
    name = input("Enter name = ")
    marks = []
    number_of_marks = int(input("Enter number of marks to add = "))
    for __ in range(0, number_of_marks):
        m = int(input("Enter mark = "))
        marks.append(m)
        student.update({name: marks})
        student[name] = marks
print(student)
