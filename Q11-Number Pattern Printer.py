# A simple pattern program with previews in the menu
def q11_pattern_generator():
    """
    Shows a menu with small examples of patterns and prints the chosen one.
    """
    while True:
        print("\n--- PATTERN MENU ---")
        print("1. Increment (1, 12, 123)")
        print("2. Repeating  (1, 22, 333)")
        print("3. Inverted   (321, 21, 1)")
        print("4. Mirror     (1, 121, 12321)")
        print("5. Exit")
        
        choice = input("\nPick a pattern (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        try:
            height = int(input("How tall should it be?: "))
            print("\nResult:")

            # Pattern 1
            if choice == "1":
                for r in range(1, height + 1):
                    for c in range(1, r + 1):
                        print(c, end="")
                    print()

            # Pattern 2
            elif choice == "2":
                for r in range(1, height + 1):
                    for c in range(1, r + 1):
                        print(r, end="")
                    print()

            # Pattern 3
            elif choice == "3":
                for r in range(height, 0, -1):
                    for c in range(r, 0, -1):
                        print(c, end="")
                    print()

            # Pattern 4
            elif choice == "4":
                for r in range(1, height + 1):
                    # Up
                    for c in range(1, r + 1):
                        print(c, end="")
                    # Down
                    for c in range(r - 1, 0, -1):
                        print(c, end="")
                    print()

            else:
                print("Invalid choice, try again.")

        except ValueError:
            print("Error: Please enter a whole number for height.")

# Start the program
q11_pattern_generator()