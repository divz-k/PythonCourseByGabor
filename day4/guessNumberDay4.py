import random

def get_random_number():
    """Generates a random number between 1 and 20."""
    return random.randint(1, 20)

def get_user_guess():
    """Prompts the user for their guess and handles special commands."""
    guess = input("Enter your guess (1-20), or 'x' to quit, 'n' to start a new game, 's' to cheat: ").lower()
    
    if guess == 'x':
        print("Exiting the game. Goodbye!")
        return None
    elif guess == 'n':
        print("Starting a new game...")
        return 'n'  # special flag to signal new game
    elif guess == 's':
        return 's'  # special flag to signal cheat mode
    
    try:
        guess = int(guess)
        if 1 <= guess <= 20:
            return guess
        else:
            print("Please enter a number between 1 and 20.")
            return get_user_guess()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_guess()

def play_game():
    """Plays one round of the number guessing game."""
    hidden_number = get_random_number()
    guesses = 0
    while True:
        guess = get_user_guess()
        
        if guess is None:  # User wants to quit the game
            return False
        if guess == 'n':  # User wants to start a new game
            return True
        if guess == 's':  # User wants to cheat
            print(f"The hidden number is {hidden_number}.")
            continue
        
        guesses += 1
        
        if guess < hidden_number:
            print("Too small!")
        elif guess > hidden_number:
            print("Too big!")
        else:
            print(f"Correct! The number was {hidden_number}.")
            print(f"You guessed it in {guesses} attempts!")
            return True

def main():
    """Main function to manage multiple games."""
    print("Welcome to the Number Guessing Game!")
    
    while True:
        if not play_game():
            break
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
