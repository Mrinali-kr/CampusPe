import random

def guess_the_number():
    # This keeps track of the lowest number of tries to win
    best_score = None 

    while True:
        # Pick a secret number between 1 and 100
        secret_number = random.randint(1, 100)
        max_tries = 7
        tries_used = 0
        is_winner = False

        print("\n" + "="*30)
        print("   NUMBER GUESSING GAME ")
        print("="*30)
        print("I am thinking of a number from 1 to 100.")
        
        if best_score:
            print(f"Current Best Score: {best_score} tries")
        
        # Give the user 7 chances
        while tries_used < max_tries:
            try:
                chances_left = max_tries - tries_used
                print(f"\nChances left: {chances_left}")
                
                guess = int(input("What is your guess?: "))
                tries_used += 1

                # Check if the guess is right
                if guess == secret_number:
                    print(f"Great job! You found it in {tries_used} tries.")
                    is_winner = True
                    
                    # Update the best score if this was faster
                    if best_score is None or tries_used < best_score:
                        best_score = tries_used
                        print("New Personal Best!")
                    break

                # Give a hint: Higher or Lower
                if guess < secret_number:
                    print("Too low!")
                else:
                    print("Too high!")

                # Bonus hint: If the user is very close (within 5)
                if abs(guess - secret_number) <= 5:
                    print("Hint: You are very close! (Within 5 numbers)")

            except ValueError:
                print("Error: Please type a whole number.")
                continue

        # If the user runs out of tries
        if not is_winner:
            print(f"\nGame Over! You used all your chances.")
            print(f"The number was: {secret_number}")

        # Ask to play another round
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again != 'yes' and again != 'y':
            print("Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    guess_the_number()