
#######################################################
# wordle_engine
#########################################################


# Container for color control codes.
class wordle_colors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

wordle_alphabet = "abcdefghijklmnopqrstuvwxyz"

def welcome_string():
    return f"""Welcome to {wordle_colors.GREEN}W{wordle_colors.RED}o{wordle_colors.BLUE}r\
{wordle_colors.YELLOW}d{wordle_colors.CYAN}l{wordle_colors.MAGENTA}e{wordle_colors.ENDC}"""

def create_letter_status():
    """ Initialize and Return a new dictionary that maps each letter to
        wordle_colors.BLUE """
    # INITIALIZE DICTIONARY THAT POINTS TO BLUE
    blue_dictionary = {}  # create empty dict
    for x in wordle_alphabet:  # loop through dict
        blue_dictionary.update({x: f"{wordle_colors.BLUE}"})  # each letter points to blue
    return blue_dictionary  # return the dict

def load_words(filename: str):
    """ Load the words from the specified file and place them
        in a set.
        Ignore any lines that begin with "#"
        """
    # CREATES THE VALID WORDS
    words_set = set(open(filename))  # opens the specified file
    new_set = []  # creates new list
    for word in words_set:  # loop the list, getting rid of line breaks
        if word[0] != "#":  # makes sure the line doesnt start with #
            word = word.rstrip()
            new_set.append(word)  # add to new list
    new_set = set(new_set)  # make the list into a set
    return new_set


def format_guess(target, guess):  # FORMATS USER'S GUESS
    """ Return a string that contains the user's guess formatted
        so that each letter is colored
        * GREEN:  The letter is placed correctly.
        * YELLOW: The letter appears in the target word,
                  but in a different location.
        * RED:    The letter does not appear in the target word
        Also, the string should end with wordle_colors.ENDC """
    target = list(target)  # target into list
    guess = list(guess)  # guess into list
    count_green = 0
    count_yellow = 0
    # GREEN
    for x in guess:  # iterate the word
        if guess[count_green] == target[count_green]:  # if same letter in same place
            guess[count_green] = f"{wordle_colors.GREEN}{x}"  # color in guess
            target[count_green] = f"{wordle_colors.GREEN}{x}"  # color in target
        count_green += 1  # to keep track of place in guess
    # YELLOW
    for k in guess:  # iterate the guess
        if k in target:  # if letter in target
            guess[count_yellow] = f"{wordle_colors.YELLOW}{k}"  # change color to yellow
        else:  # if not yellow or green
            if k.isalpha():  # ensure not referring to something thats been colored
                guess[count_yellow] = f"{wordle_colors.RED}{k}"  # make it red
        count_yellow += 1  # to keep track of place in guess
    # FORMAT
    guess.append(wordle_colors.ENDC)  # add to end of word to complete color
    guess_joined = "".join(guess)
    return guess_joined  # returns a dictionary

def update_letter_status(letter_status, target, guess):  # UPDATES USER DICTIONARY
    """ Update the letter status dictionary to show which letters
        have been used and whether they appear in the target word.
        Specifically:
        * BLUE:   Letter has not been used in a guess
        * GREEN:  Letter appears in the correct location in some guess.
        * YELLOW: Letter is in the target word and appears in some guess
                  (but not in the correct location)
        * RED:    Letter does  not appear in the target word, but has
                  been used in at least one guess."""
    letter_status = dict(letter_status)  # ensures its a dictionary
    target = list(target)  # makes target into list
    guess = list(guess)  # makes guess into list
    count = 0
    # YELLOW
    for x in guess:  # iterate guess
        if x in target:  # if letter in target
            letter_status[x] = f"{wordle_colors.YELLOW}"  # make it yellow
        else:  # if not yellow or green
            if x in letter_status.keys():
                letter_status[x] = f"{wordle_colors.RED}"  # make it red
    # GREEN
    while count < 5:  # iterate guess
        if guess[count] == target[count]:  # if same letter in same spot
            letter = guess[count]
            letter_status[letter] = f"{wordle_colors.GREEN}"  # make it green
        count += 1  # to keep track
    return letter_status

def format_letters(alphabet_dict):  # FORMAT DICTIONARIES
    """ Generate a string that lists all the letters of the alphabet
        colored according to the rules given in update_letter_status.
        the string should end with wordle_colors.ENDC """
    alphabet_dict = dict(alphabet_dict)  # ensure its a dict
    for x in alphabet_dict.keys():  # attach letter to color
        alphabet_dict[x] = f"{alphabet_dict[x]}{x}"
    alphabet_dict = alphabet_dict.values()  # put the values into a new dict
    joined = "".join(alphabet_dict)  # join them together
    joined = joined + f"{wordle_colors.ENDC}"  # add the end color
    return joined  # return formatted dictionary of values
