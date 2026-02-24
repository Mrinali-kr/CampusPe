def q2_calculator():
    """
    Performs basic arithmetic operations on two user-provided integers
    and displays the results in a clean, formatted manner.
    """
    try:
        # Collect user input as integers to avoid trailing decimals (.0)
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("\nResults:")
        
        # Basic arithmetic operations
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} * {num2} = {num1 * num2}")

        # Logical check for division and modulus to prevent ZeroDivisionError
        if num2 != 0:
            # Calculate division and round to 2 decimal places
            quotient = num1 / num2
            # Use the :g formatter to remove trailing zeros if the result is a whole number
            print(f"{num1} / {num2} = {round(quotient, 2):g}")
            print(f"{num1} % {num2} = {num1 % num2}")
        else:
            print("Division and Modulus: Cannot divide by zero")

        # Exponentiation (Power)
        print(f"{num1} ^ {num2} = {num1 ** num2}")

    except ValueError:
        # Error handling for non-numeric or non-integer inputs
        print("Invalid input! Please enter whole numbers.")

if __name__ == "__main__":
    q2_calculator()