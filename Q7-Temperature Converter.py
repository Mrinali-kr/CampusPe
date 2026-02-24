# A menu-driven program to convert temperatures between Celsius, Fahrenheit, and Kelvin
def main():
    """
    Main loop for the temperature converter. 
    Handles user selection, input validation, and mathematical conversions.
    """
    while True:
        # Display selection menu
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit   2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin       4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin    6. Kelvin to Fahrenheit")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")

        # Exit condition
        if choice == "7":
            print("Exiting program. Goodbye!")
            break

        try:
            # Check if the choice is valid before asking for temperature
            if choice in ["1", "2", "3", "4", "5", "6"]:
                temp = float(input("Enter temperature value: "))
            else:
                print("Invalid choice! Please select 1-7.")
                continue

            # Conversion Logic
            if choice == "1":
                # Celsius to Fahrenheit
                result = (temp * 9/5) + 32
                print(f"{temp}°C is equal to {result:.2f}°F")
            
            elif choice == "2":
                # Fahrenheit to Celsius
                result = (temp - 32) * 5/9
                print(f"{temp}°F is equal to {result:.2f}°C")
            
            elif choice == "3":
                # Celsius to Kelvin
                result = temp + 273.15
                print(f"{temp}°C is equal to {result:.2f} K")
            
            elif choice == "4":
                # Kelvin to Celsius
                result = temp - 273.15
                print(f"{temp} K is equal to {result:.2f}°C")
            
            elif choice == "5":
                # Fahrenheit to Kelvin
                result = (temp - 32) * 5/9 + 273.15
                print(f"{temp}°F is equal to {result:.2f} K")
            
            elif choice == "6":
                # Kelvin to Fahrenheit
                result = (temp - 273.15) * 9/5 + 32
                print(f"{temp} K is equal to {result:.2f}°F")

        except ValueError:
            # Handles non-numeric temperature inputs
            print("Error: Please enter a valid numeric temperature.")

if __name__ == "__main__":
    main()