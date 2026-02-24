# Function 1: Factorial (n!)
def factorial(n):
    if n < 0: return "Error"
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# Function 2: Prime Check
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# Function 3: Nth Fibonacci number (0, 1, 1, 2, 3, 5...)
def fibonacci(n):
    if n <= 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Function 4: Sum of Digits (123 -> 1+2+3 = 6)
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# Function 5: Reverse Number (123 -> 321)
def reverse_number(n):
    s = str(abs(n))
    rev = int(s[::-1])
    return -rev if n < 0 else rev

# Function 6: Armstrong Number (153 -> 1^3 + 5^3 + 3^3 = 153)
def is_armstrong(n):
    s = str(abs(n))
    power = len(s)
    total = sum(int(digit)**power for digit in s)
    return total == n

# Function 7: Greatest Common Divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function 8: Least Common Multiple (LCM)
def lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)

# Function 9: Perfect Number (6 -> 1+2+3 = 6)
def is_perfect_number(n):
    if n < 1: return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Function 10: Main Menu
def math_menu():
    while True:
        print("\n--- NUMBER SYSTEM MENU ---")
        print("1. Factorial      2. Prime Check   3. Fibonacci")
        print("4. Sum of Digits  5. Reverse Num   6. Armstrong Check")
        print("7. GCD            8. LCM           9. Perfect Number")
        print("10. Exit")
        
        choice = input("\nSelect an option (1-10): ")

        if choice == "10":
            print("Goodbye!")
            break

        try:
            if choice in ["1", "2", "3", "4", "5", "6", "9"]:
                n = int(input("Enter number: "))
                if choice == "1": print(f"Result: {factorial(n)}")
                elif choice == "2": print(f"Is Prime? {'Yes' if is_prime(n) else 'No'}")
                elif choice == "3": print(f"Fibonacci({n}): {fibonacci(n)}")
                elif choice == "4": print(f"Sum of digits: {sum_of_digits(n)}")
                elif choice == "5": print(f"Reversed: {reverse_number(n)}")
                elif choice == "6": print(f"Is Armstrong? {'Yes' if is_armstrong(n) else 'No'}")
                elif choice == "9": print(f"Is Perfect? {'Yes' if is_perfect_number(n) else 'No'}")
            
            elif choice in ["7", "8"]:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                if choice == "7": print(f"GCD: {gcd(a, b)}")
                elif choice == "8": print(f"LCM: {lcm(a, b)}")
            
            else:
                print("Invalid choice!")
        except ValueError:
            print("Error: Please enter whole numbers only.")

if __name__ == "__main__":
    math_menu()