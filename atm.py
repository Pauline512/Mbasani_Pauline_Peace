# Initial account balance
balance = 1000  

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print(f"Your current balance is: UGX {balance}")
    
    elif choice == "2":
        amount = int(input("Enter amount to withdraw: UGX "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful! UGX {amount} withdrawn.")
            print(f"Remaining balance: UGX {balance}")
        else:
            print("Insufficient funds. Withdrawal denied.")
    
    elif choice == "3":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")