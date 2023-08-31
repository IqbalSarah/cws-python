# # Electricity bill

x = int(input("Enter units = "))
y = int(input("Enter rate = "))
total_cost = x * y + (12 / 100 * (x * y))
if total_cost > 100 and total_cost % 5 == 0:
    print(
        f"The cost of your light bill is ${total_cost}. There is a free gift card to your favorite store."
    )
else:
    print(f"The cost of your light bill is ${total_cost}")


# """Electricity bill according to given conditions
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill"""

unit = int(input("Enter electricity units = "))
if unit <= 50 and unit > 0:
    total = 0.50 * unit
elif unit >= 51 and unit <= 150:
    total = 50 * 0.50 + ((unit - 50) * 0.75)
elif unit >= 151 and unit <= 250:
    total = 0.50 * 50 + 0.75 * 100 + ((unit - 150) * 1.20)
else:
    total = 0.50 * 50 + 0.75 * 100 + 0.75 * 100 + ((unit - 250) * 1.50)
surcharge = total * 0.20
total = total + surcharge
print(f"Total bill ={total}")


# To check the triangle is isosceles, scalene, equilateral and right angled by entering angles of triangle

a = float(input("Enter the first angle of the triangle: "))
b = float(input("Enter the second angle of the triangle: "))
c = float(input("Enter the third angle of the triangle: "))
if a + b + c != 180:
    print("Not a valid triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right-angled triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")

# Absolute value of a given number

num = int(input("Enter the value : "))
absolute = abs(num)
print("The absolute value of %d is %d" % (num, absolute))

# Checking if a character is vowel or consonant

char = str(input("Enter the character : ")).lower()
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")


# Largest among three given numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a > b and a > c:
    print(f"{a} is the largest number")
elif b > a and b > c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")
