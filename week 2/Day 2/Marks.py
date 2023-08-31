"""
Ask 3 marks from user. Out of 100

If pass in all subjects
Then only print total and percentage

FAIL
"""

Sub1 = int(input("Enter marks:"))
Sub2 = int(input("Enter marks:"))
Sub3 = int(input("Enter marks:"))
if Sub1 >= 33 and Sub2 >= 33 and Sub3 >= 33:
    total_marks = Sub1 + Sub2 + Sub3
    total_percentage = (total_marks / 300) * 100
    print(f"total = {total_marks} and percentage scored = {total_percentage:.2f} % ")
else:
    print("Fail")
