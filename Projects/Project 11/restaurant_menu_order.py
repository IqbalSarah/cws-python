menu = {"Burger": 5.00, "Pizza": 10.00, "Salad": 7.00}

order = []

while True:
    print("\nMenu:")
    print("1. View the menu")
    print("2. Add an item to the order")
    print("3. Calculate the total cost")
    print("4. Exit")

    choice = input("Please choose an option (1-4): ")

    if choice == "1":
        print("Menu Items:")
        for item, price in menu.items():
            print(f"{item}: {price:.2f}")

    elif choice == "2":
        item = input("Enter the item you want to add to your order: ")
        if item in menu:
            order.append(item)
            print(f"{item} has been added to your order.")
        else:
            print(f"{item} is not on the menu.")

    elif choice == "3":
        total_cost = 0
        for item in order:
            total_cost += menu.get(item, 0)
        print(f"Total cost of your order: ${total_cost:.2f}")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please choose a valid option (1-4).")

print("Thank you for using our restaurant menu and order system. Goodbye!")
