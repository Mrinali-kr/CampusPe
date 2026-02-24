# Function to check if a number is prime
def is_prime(num):
    """
    Returns True if a number is prime, False otherwise.
    Handles negative numbers, 0, and 1.
    """
    if num <= 1:
        return False
    if num == 2:
        return True
    
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def q15_prime_suite():
    try:
        # Part 1: Single Number Check
        n = int(input("Enter a number: "))
        if is_prime(n):
            print(f"{n} is a PRIME number")
        else:
            print(f"{n} is NOT a prime number")

        # Part 2: Range Finder
        start = int(input("\nEnter start range: "))
        end = int(input("Enter end range: "))
        
        prime_list = []
        for val in range(start, end + 1):
            if is_prime(val):
                prime_list.append(str(val))
        
        # Display the found primes separated by commas
        if prime_list:
            print(f"Prime numbers: {', '.join(prime_list)}")
        else:
            print("No prime numbers found in this range.")

    except ValueError:
        print("Invalid input! Please enter whole numbers.")

if __name__ == "__main__":
    q15_prime_suite()