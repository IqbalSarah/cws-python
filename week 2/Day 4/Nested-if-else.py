"""
Ask a number from user, print positive negative or zero

if condition:
    if condition2:
        ...
        ...
    else:
        ...
else:
    if condition3:
        ...
        ...
        ...
    elif 
"""
number = int(input("Enter a number = "))
if number >= 0:
    if number == 0:
        print("Equal to zero")
    else:
        print("Positive")
else:
    print("Negative")
