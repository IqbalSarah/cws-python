password = input("Please enter a password: ")

length = len(password) >= 8
uppercase = 0
lowercase = 0
digit = 0
special_char = 0

for char in password:
    if char.isupper():
        uppercase = 1
    elif char.islower():
        lowercase = 1
    elif char.isdigit():
        digit = 1
    elif char in "!@#$%^&*":
        special_char = 1

criteria_count = length + uppercase + lowercase + digit + special_char

if criteria_count <= 2:
    strength = "Weak"
elif criteria_count <= 4:
    strength = "Moderate"
else:
    strength = "Strong"
print(f"The password strength is '{strength}'")
