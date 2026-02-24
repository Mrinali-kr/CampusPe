# Program to determine if a year is a leap year with logical explanations
def q7_leap_year_checker():
    """
    Checks if a year is a leap year based on the Gregorian calendar rules
    and provides a specific reason for the result.
    """
    try:
        # Get year input from the user
        year = int(input("Enter year: "))
        
        # Rule 1: Divisible by 4
        # Rule 2: If divisible by 100, must also be divisible by 400
        
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    # Divisible by 4, 100, and 400
                    is_leap = True
                    reason = "it is divisible by 400."
                else:
                    # Divisible by 4 and 100, but not 400
                    is_leap = False
                    reason = "it is divisible by 100 but not by 400."
            else:
                # Divisible by 4 but not by 100
                is_leap = True
                reason = "it is divisible by 4 and not by 100."
        else:
            # Not divisible by 4 at all
            is_leap = False
            reason = "it is not divisible by 4."

        # Display the formatted output
        status = "is a Leap Year" if is_leap else "is NOT a Leap Year"
        print(f"\nYear: {year}")
        print(f"Status: {status}")
        print(f"Reason: Because {reason}")

    except ValueError:
        print("Invalid input! Please enter a whole number for the year.")

if __name__ == "__main__":
    q7_leap_year_checker()