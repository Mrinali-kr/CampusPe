# Program to print multiplication tables
def q12_multiplication_tables():
    """
    Prints a specific table based on user input and a 10x10 grid.
    """
    try:
        # Part 1: Specific Table
        num = int(input("Enter number: "))
        table_range = int(input("Enter range (end): "))

        print(f"\nMultiplication Table of {num}")
        for i in range(1, table_range + 1):
            print(f"{num} x {i} = {num * i}")

        # Part 2: Bonus - 10x10 Grid
        print("\n" + "="*40)
        print("BONUS: FULL 1-10 MULTIPLICATION GRID")
        print("="*40)

        # Print the grid
        for row in range(1, 11):
            for col in range(1, 11):
                # {value:4} keeps the columns aligned by giving each number 4 spaces
                print(f"{row * col:4}", end="")
            print() # Move to the next row

    except ValueError:
        print("Error: Please enter whole numbers only.")

if __name__ == "__main__":
    q12_multiplication_tables()