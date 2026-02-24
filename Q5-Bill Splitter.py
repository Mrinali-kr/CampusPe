# Calculates and splits a restaurant bill including tax and tip
def q4_bill_splitter():
    """
    Calculates subtotal, tax, tip, and total bill, 
    then splits the final amount among a specified number of people.
    """
    try:
        # Collect user input for bill components
        bill_subtotal = float(input("Enter total bill: "))
        num_people    = int(input("Number of people: "))
        tax_percent   = float(input("Tax percentage: "))
        tip_percent   = float(input("Tip percentage: "))

        # Validation to prevent division by zero or negative people
        if num_people <= 0:
            print("Error: Number of people must be at least 1.")
            return

        # Perform financial calculations
        tax_amount  = bill_subtotal * (tax_percent / 100)
        after_tax   = bill_subtotal + tax_amount
        # Tip is typically calculated on the post-tax amount
        tip_amount  = after_tax * (tip_percent / 100)
        total_bill  = after_tax + tip_amount
        per_person  = total_bill / num_people

        # Display formatted breakdown
        print("\n=== BILL BREAKDOWN ===")
        # :<12 aligns text to the left, while .2f ensures 2 decimal places
        print(f"{'Subtotal:':<12} ₹{bill_subtotal:.2f}")
        print(f"{f'Tax ({tax_percent:g}%):':<12} ₹{tax_amount:.2f}")
        print(f"{'After tax:':<12} ₹{after_tax:.2f}")
        print(f"{f'Tip ({tip_percent:g}%):':<12} ₹{tip_amount:.2f}")
        print(f"{'Total:':<12} \n₹{total_bill:.2f}")
        print(f"{'Per person:':<12} ₹{per_person:.2f}")

    except ValueError:
        # Handle non-numeric inputs
        print("Invalid input! Please enter numeric values for the bill, tax, and tip.")

if __name__ == "__main__":
    q4_bill_splitter()