# Adding two numbers entered by User

num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))
sum = num1 + num2
print(sum)

# convert kilometers to miles

km = float(input("Enter kilometer : "))
miles = km * 0.621371
print(f"{km} kms = {miles} miles")

# Calculating the Average of 3 numbers

a = float(input("Enter number 1 : "))
b = float(input("Enter number 2 : "))
c = float(input("Enter number 3 : "))
average = (a + b + c) / 3
print(f"The average of {a}, {b} and {c} is {average} ")

# Converting rupees to paise

rupees = float(input("Enter rupees : "))
paise = rupees * 100
print(f"{rupees} rupees = {paise} paise")

# Area of Square

a = float(input("Enter sides of the square : "))
A = a**2
print(f"The area of the square is {A}")


# Calculating number of tie and total points of game

number_of_games_played = int(input("Enter number of games played : "))
wonGames = int(input("Enter number of games won : "))
lostGames = int(input("Enter number of games lost : "))
tieGames = number_of_games_played - (wonGames + lostGames)
totalPoints = wonGames * 4 + tieGames * 2
print("Number of tie games =", tieGames, ", Total points =", totalPoints)
