# Number Guessing Game
# Requirements:
#  Uses a function named guessing_game
#  Asks user to guess a number (1, 100)
#  Tell user if their guess is too high or too low
#    Re-guess if incorrect
#    Exit if correct

import random
from random import randint

def guessing_game():
    # Set game_state to 1 for game on, 0 for game over
    game_state = 1
    # Set starting number of guesses to 0
    guesses = 1
    # Set the random int
    winning_number = randint(1, 100)

    # Main loop of the game
    print("Let's play a number guessing game!\n")
    while game_state == 1:
        # Get the player's guess and verify it's an integer, if not ask them to input an integer
        player_guess = input("Guess a number between 1 and 100: ")

        # Verify that the response entered is an integer, if not loop around
        try:
            player_guess = int(player_guess)

            # If it is an int, run the check if/elif/else
            if player_guess > winning_number:
                print(f"Sorry, that's too high!")
                guesses += 1
            elif player_guess < winning_number:
                print(f"Sorry, that's too low!")
                guesses += 1
            else:
                print(f"The winning number was {winning_number}! You win with guess total: {guesses}!")
                game_state = 0
        except ValueError as e:
            print("Please input an integer between 1 and 100.")
        

if __name__ == '__main__':
    guessing_game()