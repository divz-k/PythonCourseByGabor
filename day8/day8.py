import tkinter as tk
from tkinter import messagebox
import random

# Function to generate a random number
def get_random_number():
    """Generates a random number between 1 and 20."""
    return random.randint(1, 20)

# Function to check the guess
def check_guess():
    """Check the user's guess and update the game state."""
    global hidden_number, guesses
    try:
        guess = int(entry_guess.get())  # Get the user's guess from the entry field
        
        if 1 <= guess <= 20:
            guesses += 1
            if guess < hidden_number:
                label_message.config(text="Too small!")
            elif guess > hidden_number:
                label_message.config(text="Too big!")
            else:
                label_message.config(text=f"Correct! The number was {hidden_number}.")
                messagebox.showinfo("Game Over", f"You guessed it in {guesses} attempts!")
                reset_game()
        else:
            label_message.config(text="Please enter a number between 1 and 20.")
    except ValueError:
        label_message.config(text="Invalid input. Please enter a valid number.")

# Function to start a new game
def start_new_game():
    """Reset the game state for a new round."""
    global hidden_number, guesses
    hidden_number = get_random_number()  # Generate a new random number
    guesses = 0  # Reset the guess count
    label_message.config(text="Guess a number between 1 and 20!")
    entry_guess.delete(0, tk.END)  # Clear the input field

# Function to reset the game
def reset_game():
    """Reset the game state without changing the random number."""
    entry_guess.delete(0, tk.END)
    label_message.config(text="Game Over. Start a new game!")

# Setting up the GUI window
root = tk.Tk()
root.title("Number Guessing Game")

# Initialize game variables
hidden_number = get_random_number()
guesses = 0

# Create and place widgets
label_title = tk.Label(root, text="Welcome to the Number Guessing Game!", font=("Arial", 16))
label_title.pack(pady=10)

label_message = tk.Label(root, text="Guess a number between 1 and 20!", font=("Arial", 14))
label_message.pack(pady=10)

entry_guess = tk.Entry(root, font=("Arial", 14))
entry_guess.pack(pady=10)

button_guess = tk.Button(root, text="Submit Guess", font=("Arial", 14), command=check_guess)
button_guess.pack(pady=5)

button_new_game = tk.Button(root, text="Start New Game", font=("Arial", 14), command=start_new_game)
button_new_game.pack(pady=5)

button_exit = tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit)
button_exit.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
