from datetime import datetime

def q3_age_metrics():
    """
    Calculates precise age metrics from a specific birth date 
    and displays them in a numbered list format.
    """
    try:
        # Prompt user for specific date components
        year  = int(input("Enter birth year (YYYY): "))
        month = int(input("Enter birth month (1-12): "))
        day   = int(input("Enter birth day (1-31): "))

        # Initialize date objects
        birth_date = datetime(year, month, day)
        now = datetime.now()

        # Validation to ensure date is in the past
        if birth_date > now:
            print("Error: Birth date cannot be in the future.")
            return

        # Calculate exact years (checking if birthday has occurred this year)
        age_years = now.year - birth_date.year
        if (now.month, now.day) < (birth_date.month, birth_date.day):
            age_years -= 1

        # Calculate time differences for months, days, hours, and minutes
        diff = now - birth_date
        total_days = diff.days
        total_hours = total_days * 24
        total_minutes = total_hours * 60
        total_months = (age_years * 12) + (now.month - birth_date.month)

        # Output results in a numbered list format
        print(f"\nResults for birth date {birth_date.strftime('%Y-%m-%d')}:")
        print(f"1. Current age: {age_years}")
        print(f"2. Age in months: {total_months}")
        print(f"3. Age in days (approx 365 days/year): {total_days}")
        print(f"4. Age in hours: {total_hours}")
        print(f"5. Age in minutes: {total_minutes}")
        print(f"6. Years until age 100: {100 - age_years}")

    except ValueError:
        print("Invalid input! Please enter numeric values for year, month, and day.")

if __name__ == "__main__":
    q3_age_metrics()