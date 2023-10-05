products = {}


def addProduct():
    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    products[product_id] = {"name": product_name, "quantity": quantity, "price": price}
    print(f"Product '{product_name}' added successfully!")


def updateProduct():
    product_id = input("Enter product ID to update: ")
    if product_id in products:
        product_name = input("Enter updated product name: ")
        quantity = int(input("Enter updated quantity: "))
        price = float(input("Enter updated price: "))
        products[product_id] = {
            "name": product_name,
            "quantity": quantity,
            "price": price,
        }
        print(f"Product '{product_name}' updated successfully!")
    else:
        print("Product not found.")


def deleteProduct():
    product_id = input("Enter product ID to delete: ")
    if product_id in products:
        product_name = products[product_id]["name"]
        del products[product_id]
        print(f"Product '{product_name}' deleted successfully!")
    else:
        print("Product not found.")


def viewProducts():
    if not products:
        print("No products in the inventory.")
    else:
        print("Inventory:")
        for product_id, product_info in products.items():
            print(f"Product ID: {product_id}")
            print(f"Product Name: {product_info['name']}")
            print(f"Quantity: {product_info['quantity']}")
            print(f"Price: ${product_info['price']:.2f}")
            print("----------------------------")


while True:
    print("\nMenu:")
    print("1. Add a product")
    print("2. Update a product")
    print("3. Delete a product")
    print("4. View all products")
    print("5. Exit")

    choice = input("Please choose an option (1-5): ")

    if choice == "1":
        addProduct()
    elif choice == "2":
        updateProduct()
    elif choice == "3":
        deleteProduct()
    elif choice == "4":
        viewProducts()
    elif choice == "5":
        print("Exiting the inventory management system.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1-5).")
