# Checking if a character is vowel or consonant

char = str(input("Enter the character : ")).lower()
if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")


# Checking even and odd numbers

num = int(input("Enter the number : "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# Multiple of 3 and 5

num = int(input("Enter the number : "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is multiple of 3 and 5")
else:
    print(f"{num} is not multiple of 3 and 5")


# Comparing two numbers and print the larger number

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if a > b:
    print(f"{a} is larger")
else:
    print(f"{b} is larger")


# Absolute value of a given number

num = int(input("Enter the value : "))
absolute = abs(num)
print("The absolute value of %d is %d" % (num, absolute))


# Greatest among three given numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a > b and a > c:
    print(f"{a} is the greatest number")
elif b > a and b > c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")


# Calculating total bill of hotel stay

x = float(input("Enter room rate per night : "))
y = int(input("Enter number of nights stayed : "))
total_cost = x * y + (10 / 100 * (x * y))
print(f"Your total bill is {total_cost} ")


# Calculating highest, lowest and average scores among friend's dishes

Score_of_friend1 = a = 7
Score_of_friend2 = b = 9
Score_of_friend3 = c = 6
Score_of_friend4 = d = 8
Score_of_friend5 = e = 7

if a > b and a > c and a > d and a > e:
    print(a, "has the highest score")
elif b > a and b > c and b > d and b > e:
    print(b, "has the highest score")
elif c > a and c > b and c > d and c > e:
    print(c, "has the highest score")
elif d > a and d > b and d > c and d > e:
    print(d, "has the highest score")
else:
    print(e, "has the highest score")
