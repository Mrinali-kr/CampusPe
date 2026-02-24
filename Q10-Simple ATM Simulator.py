# Simulates basic ATM operations including balance checks, deposits, and withdrawals
def q10_atm_simulator():
    """
    Manages a virtual bank account with a starting balance of ₹10,000.
    Enforces a minimum balance of ₹500 and validates all inputs.
    """
    balance = 10000.0
    MINIMUM_BALANCE = 500.0

    print("--- WELCOME TO CAMPUSPE ATM ---")

    while True:
        # Display the menu options
        print("\nATM SIMULATOR")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                # Display current available balance
                print(f"Current balance: ₹{balance:,.2f}")

            elif choice == "2":
                # Handle money deposit
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"Deposit successful! ₹{amount:,.2f} added to your account.")
                    print(f"New balance: ₹{balance:,.2f}")
                else:
                    print("Error: Deposit amount must be positive.")

            elif choice == "3":
                # Handle money withdrawal with minimum balance check
                amount = float(input("Enter amount to withdraw: "))
                
                if amount <= 0:
                    print("Error: Withdrawal amount must be positive.")
                elif balance - amount < MINIMUM_BALANCE:
                    # Enforce the rule that ₹500 must always remain
                    print("Transaction Failed!")
                    print(f"Reason: Insufficient funds. A minimum balance of ₹{MINIMUM_BALANCE} is required.")
                else:
                    balance -= amount
                    print("Withdrawal successful!")
                    print(f"New balance: ₹{balance:,.2f}")

            elif choice == "4":
                # Exit the simulation
                print("Thank you for using our ATM. Have a great day!")
                break

            else:
                print("Invalid choice! Please select an option from 1 to 4.")

        except ValueError:
            # Handle non-numeric inputs for amounts
            print("Error: Please enter a valid numeric value.")

if __name__ == "__main__":
    q10_atm_simulator()