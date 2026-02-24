def q1_bio_card():
    # Ask for user input
    print("Please enter the following details:")
    name    = input("Name: ")
    age     = input("Age: ")
    course  = input("Course: ")
    college = input("College: ")
    email   = input("Email: ")

    # Format age to include "years"
    age_str = f"{age} years"

    # Print the formatted box card
    print("\n" + "╔════════════════════════════════╗")
    print("║       STUDENT BIO CARD         ║")
    print("╠════════════════════════════════╣")
    # Using .ljust() or f-string padding to keep the right border aligned
    print(f"║  Name    : {name[:20]:<20} ║")
    print(f"║  Age     : {age_str[:20]:<20} ║")
    print(f"║  Course  : {course[:20]:<20} ║")
    print(f"║  College : {college[:20]:<20} ║")
    print(f"║  Email   : {email[:20]:<20} ║")
    print("╚════════════════════════════════╝")

# Call the function to test it
q1_bio_card()