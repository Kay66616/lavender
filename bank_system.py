# Simple ATM System

PIN = "1234"
balance = 1000.00
transactions = []

print("Welcome to the ATM!")

# PIN Validation
pin = input("Enter your 4-digit PIN: ")

if pin != PIN:
    print("Incorrect PIN. Exiting system.")
else:
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"\nYour balance is ${balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                transactions.append(f"Deposited: ${amount:.2f}")
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Invalid amount. Deposit must be positive.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance.")
            elif amount > 0:
                balance -= amount
                transactions.append(f"Withdrew: ${amount:.2f}")
                print(f"${amount:.2f} withdrawn successfully.")
            else:
                print("Invalid amount. Withdrawal must be positive.")

        elif choice == "4":
            print("\nTransaction History:")
            if not transactions:
                print("No transactions yet.")
            else:
                for transaction in transactions:
                    print(transaction)

        elif choice == "5":
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")
