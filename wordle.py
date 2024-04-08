
#######################################################
# wordle
#########################################################

# This is the "main" portion of your game.
# Any code that uses stdin or stdout (i.e., input() and print())
# should go in this file.

import wordle_engine
import random
import sys


# Print a greeting
print(wordle_engine.welcome_string())

# Load the list of valid words
valid_words = wordle_engine.load_words("combined_wordlist.txt")

# Use the target word provided on the command line,
# or, choose a random word if no target word given.
if len(sys.argv) >= 2:
    target = sys.argv[1]
else:
    # choose a random word from valid_words
    target = random.choice(list(valid_words))

# TODO Implement the rest of the game.
# Remember:
#   * Guesses must be exactly 5 letters
#   * Guesses must be valid words
#   * Players get at most 6 guesses
#   * Please display the entire history of guesses before each prompt.
#   * Print a message at the end of the game indicating whether the player won or lost.
#      * If the player wins, display the entire sequence of guesses as part of the final message.

# SET UP THE GAME
turn = 6
guesses = []
blue_dict = wordle_engine.create_letter_status()
updated_alpha = blue_dict
print(wordle_engine.format_letters(blue_dict))
# KEEP TRACK OF TURNS
while turn > 0:
    user_input = input("Please enter a word or enter to quit: ")  # get user input
    if user_input == "":  # if they want to quit, user presses enter
        break
    if len(user_input) == 5:  # ensure input is 5 letters
        if user_input in valid_words:  # ensure input is a recognized word
            # FORMATS THE GUESS PROPERLY
            turn -= 1
            guess_formatted = wordle_engine.format_guess(target, user_input)
            # ADD GUESS TO LIST OF GUESSES
            guesses.append(guess_formatted)
            # UPDATE AND FORMAT THE ALPHABET
            updated_alpha = wordle_engine.update_letter_status(updated_alpha, target, user_input)
            formatted_dict = wordle_engine.format_letters(updated_alpha)
            print(formatted_dict)
            # PRINT GUESSES
            for x in guesses:
                print(x)
            # IF YOU WON THE GAME
            if user_input == target:
                print("You guessed right! Good job!")
                print("These were your guesses throughout the game: ")
                for x in guesses:
                    print(x)
                break
            # IF YOU LOST THE GAME
            if turn == 0:
                print(f"You're out of turns! The word was {target}! Play again!")
                break
        else:
            print("Wordle does not recognize that word. Please try again.")
    else:
        print("Wordle only accepts 5 letter words. Please try again.")
