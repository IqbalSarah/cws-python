"""
Ask 1 mark

91-100 -> A
81-90 -> B
71-80 -> C
61-70 -> D
0-60 -> E

Invalid
we can also write like this 91<=marks<=100:
"""

mark = float(input("Enter marks : "))
if mark >= 91 and mark <= 100:
    print("Your grade is A")
elif mark >= 81 and mark <= 90:
    print("Your grade is B")
elif mark >= 71 and mark <= 80:
    print("Your grade is C")
elif mark >= 61 and mark <= 70:
    print("Your grade is D")
elif mark >= 0 and mark <= 60:
    print("Your grade is E")
else:
    print("Invalid")
