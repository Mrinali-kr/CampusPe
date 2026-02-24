# Program to calculate factorial with step-by-step display
def q14_factorial_calculator():
    """
    Calculates the factorial of a number and shows the 
    multiplication steps (e.g., 5 x 4 x 3 x 2 x 1).
    """
    try:
        n = int(input("Enter a number: "))

        # Rule: Factorial is not defined for negative numbers
        if n < 0:
            print("Error: Factorial is not defined for negative numbers.")
            return
        
        # Rule: Factorial of 0 is always 1
        if n == 0:
            print("0! = 1")
            return

        fact = 1
        steps = []

        # Loop to calculate factorial and store steps for display
        # We count down from n to 1 to match the sample output we are given
        for i in range(n, 0, -1):
            fact *= i
            steps.append(str(i))

        # Join the numbers with " × " to create the step-by-step string
        calculation_path = " × ".join(steps)

        # Final output
        print(f"{n}! = {calculation_path} = {fact}")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

if __name__ == "__main__":
    q14_factorial_calculator()