# Function for adding two numbers
def add(a, b):
    return a + b

# Function for subtracting two numbers
def subtract(a, b):
    return a - b

# Function for multiplying two numbers
def multiply(a, b):
    return a * b

# Function for dividing two numbers
def divide(a, b):
    # Rule: You cannot divide a number by zero
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Function to find the remainder
def modulus(a, b):
    if b == 0:
        return "Error: Cannot use modulus with zero!"
    return a % b

# Function for power (a raised to the power of b)
def power(a, b):
    return a ** b

# Main function to run the calculator
def calculator():
    while True:
        # Show the menu to the user
        print("\n--- SIMPLE CALCULATOR ---")
        print("1. Add      2. Subtract")
        print("3. Multiply 4. Divide")
        print("5. Modulus  6. Power")
        print("7. Exit")

        choice = input("\nPick an option (1-7): ")

        # Stop the program if user picks 7
        if choice == "7":
            print("Closing calculator. Goodbye!")
            break

        # Check if the choice is valid
        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                # Get the numbers for math
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Perform the correct math based on choice
                if choice == "1":
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {divide(num1, num2)}")
                elif choice == "5":
                    print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
                elif choice == "6":
                    print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")

            except ValueError:
                print("Error: Please enter a valid number.")
        else:
            print("Invalid choice. Please try again.")

# Run the calculator
if __name__ == "__main__":
    calculator()