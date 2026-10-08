balance = 50000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = int(input("Choose an option (1-4): "))
    
    if choice == 1:
        print(f"Current Balance: {balance}")
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Successfully deposited. New Balance: {balance}")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Successfully withdrew. New Balance: {balance}")
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose between 1 and 4.")