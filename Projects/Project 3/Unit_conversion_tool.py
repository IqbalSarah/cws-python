print("Menu:")
print("1. Kilometers to miles")
print("2. Miles to kilometers")
print("3. Kilograms to pounds")
print("4. Pounds to kilograms")
print("5. Celsius to Fahrenheit")
print("6. Fahrenheit to Celsius")
print("7. Exit")

choice = input("Please choose an option (1-7): ")

if choice == "1":
    value = float(input("Enter the value in kilometers: "))
    result = value * 0.621371
    print(f"{value} kilometers is equal to {result} miles")
elif choice == "2":
    value = float(input("Enter the value in miles: "))
    result = value / 0.621371
    print(f"{value} miles is equal to {result} kilometers")
elif choice == "3":
    value = float(input("Enter the value in kilograms: "))
    result = value * 2.20462
    print(f"{value} kilograms is equal to {result} pounds")
elif choice == "4":
    value = float(input("Enter the value in pounds: "))
    result = value / 2.20462
    print(f"{value} pounds is equal to {result} kilograms")
elif choice == "5":
    value = float(input("Enter the value in Celsius: "))
    result = (value * 9 / 5) + 32
    print(f"{value} Celsius is equal to {result} Fahrenheit")
elif choice == "6":
    value = float(input("Enter the value in Fahrenheit: "))
    result = (value - 32) * 5 / 9
    print(f"{value} Fahrenheit is equal to {result} Celsius")
elif choice == "7":
    print("Goodbye!")
else:
    print("Invalid choice. Please choose an option between 1 to 7")
