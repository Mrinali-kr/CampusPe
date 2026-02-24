# Movie ticket pricing system with age-based rates and weekend discounts
def q9_ticket_system():
    """
    Determines ticket cost based on age and applies a 20% discount 
    for weekend bookings (Friday-Sunday).
    """
    try:
        # Collect user inputs
        age = int(input("Enter age: "))
        day = input("Enter day of week (e.g., Monday, Friday): ").strip().lower()
        num_tickets = int(input("Number of tickets: "))

        if num_tickets <= 0:
            print("Number of tickets must be at least 1.")
            return

        # Step 1: Determine Base Price per ticket based on age
        if age < 3:
            category = "Infant"
            base_price = 0
        elif 3 <= age <= 12:
            category = "Child"
            base_price = 150
        elif 13 <= age <= 59:
            category = "Adult"
            base_price = 300
        else:
            category = "Senior"
            base_price = 200

        # Step 2: Calculate Discount logic
        # Friday, Saturday, and Sunday receive a 20% discount
        weekend_days = ["friday", "saturday", "sunday"]
        discount_rate = 0.20 if day in weekend_days else 0.0
        
        # Calculations
        subtotal_per_ticket = base_price
        discount_amount = subtotal_per_ticket * discount_rate
        final_price_per_ticket = subtotal_per_ticket - discount_amount
        total_payable = final_price_per_ticket * num_tickets

        # Step 3: Display Detailed Breakdown
        print(f"\n--- TICKET RECEIPT ({category}) ---")
        print(f"Base Price:       ₹{subtotal_per_ticket:.2f}")
        
        if discount_amount > 0:
            print(f"Weekend Discount: -₹{discount_amount:.2f} (20% off)")
        else:
            print("Discount:         ₹0.00 (Weekday Rate)")
            
        print(f"After Discount:   ₹{final_price_per_ticket:.2f} per ticket")
        print("-" * 30)
        print(f"TOTAL AMOUNT:     ₹{total_payable:.2f} (for {num_tickets} ticket/s)")

    except ValueError:
        print("Invalid input! Please enter numeric values for age and tickets.")

if __name__ == "__main__":
    q9_ticket_system()