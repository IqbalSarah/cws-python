delivery_orders = {}
order_id_counter = 1


def placeOrder():
    global order_id_counter
    customer_name = input("Enter your name: ")
    order_items = input("Enter your order items (comma-separated): ").split(",")
    delivery_address = input("Enter your delivery address: ")
    order_status = "Preparing"
    order_details = {
        "customer_name": customer_name,
        "order_items": order_items,
        "delivery_address": delivery_address,
        "status": order_status,
    }
    delivery_orders[order_id_counter] = order_details
    print(f"Order placed successfully! Your order ID is: {order_id_counter}")
    order_id_counter += 1


def trackDelivery():
    order_id = int(input("Enter your order ID: "))
    if order_id in delivery_orders:
        order_details = delivery_orders[order_id]
        print(f"Order Status: {order_details['status']}")
    else:
        print("Order not found.")


def updateDeliveryStatus():
    order_id = int(input("Enter the order ID to update: "))
    if order_id in delivery_orders:
        order_details = delivery_orders[order_id]
        print(f"Current Status: {order_details['status']}")
        new_status = input("Enter new status (Preparing/Out for Delivery/Delivered): ")
        if new_status in ["Preparing", "Out for Delivery", "Delivered"]:
            order_details["status"] = new_status
            print(f"Status updated to: {new_status}")
        else:
            print("Invalid status.")
    else:
        print("Order not found.")


def viewOrderHistory():
    customer_name = input("Enter your name: ")
    orders_found = False
    for order_id, order_details in delivery_orders.items():
        if order_details["customer_name"] == customer_name:
            print(f"Order ID: {order_id}")
            print(f"Order Items: {', '.join(order_details['order_items'])}")
            print(f"Delivery Address: {order_details['delivery_address']}")
            print(f"Status: {order_details['status']}\n")
            orders_found = True
    if not orders_found:
        print("No orders found for this customer.")


while True:
    print("\nMain Menu:")
    print("1. Place an Order")
    print("2. Track Delivery")
    print("3. Update Delivery Status")
    print("4. View Order History")
    print("5. Exit")

    choice = input("Please choose an option (1-5): ")

    if choice == "1":
        placeOrder()
    elif choice == "2":
        trackDelivery()
    elif choice == "3":
        updateDeliveryStatus()
    elif choice == "4":
        viewOrderHistory()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option (1-5).")

print("Thank you for using the Food Delivery Tracking System. Goodbye!")
