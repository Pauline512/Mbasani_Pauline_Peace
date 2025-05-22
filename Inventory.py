# Simple Inventory Management Program

# Sample stock list as a list of dictionaries
stock = [
    {"item": "Apples", "quantity": 50},
    {"item": "Bananas", "quantity": 30},
    {"item": "Oranges", "quantity": 20}
]

# Function to display all stock items
def display_stock():
    print("\n--- Current Stock ---")
    for i, product in enumerate(stock, start=1):
        print(f"{i}. {product['item']} - Quantity: {product['quantity']}")
    print()

# Function to update stock quantity
def update_stock():
    display_stock()
    try:
        choice = int(input("Enter the item number to update: ")) - 1
        if 0 <= choice < len(stock):
            new_quantity = int(input(f"Enter new quantity for {stock[choice]['item']}: "))
            stock[choice]['quantity'] = new_quantity
            print("Quantity updated successfully!\n")
        else:
            print("Invalid item number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main loop
while True:
    print("Inventory Management Menu:")
    print("1. View Stock")
    print("2. Update Stock")
    print("3. Exit")
    
    option = input("Choose an option (1-3): ")

    if option == "1":
        display_stock()
    elif option == "2":
        update_stock()
    elif option == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
