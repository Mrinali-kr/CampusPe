# Program to check if a word or number is a palindrome
def q17_palindrome_checker():
    """
    Checks if an input reads the same forward and backward.
    Works for both words and numbers.
    """
    # 1. Get input from the user
    original = input("Enter word or number: ")

    # 2. Prepare the data
    # We use .lower() to ignore case difference
    
    clean_text = original.lower()
    
    # 3. Reverse the text
    # This [::-1] is a Python trick to flip a string backward
    reversed_text = clean_text[::-1]

    # 4. Show the step-by-step verification
    print(f"\nOriginal: {original}")
    # We flip the original string exactly as typed for the "Reversed" display
    print(f"Reversed: {original[::-1]}")

    # 5. Check if they match
    if clean_text == reversed_text:
        print("Result: PALINDROME")
    else:
        print("Result: NOT A PALINDROME")

if __name__ == "__main__":
    q17_palindrome_checker()