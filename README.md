[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/bCgl85tc)
# Python MidTerm Assignment

For this project, you are going to implement a _text-based_ version of Wordle that produces colored output.

The goals of the project are to 
* Practice writing Python code using loops, dictionaries, sets, and file I/O.

## Prerequisites

  1. Learn how to play [Wordle](https://www.nytimes.com/games/wordle/index.html).  ([This video](https://www.youtube.com/watch?v=lv4Zg-209MY) may be helpful.)
  2. Watch [this demo](https://youtu.be/ITrtfavW5sk) of the program you will be creating.
  
## Color output

Your program will produce colored output. In order to change the color of text output, you need only add a special character sequence to your output string.  These special sequences are provided in the starter code.  For example, to print the string "I hate hard projects" with the word "hate" in Red, you would do this:

`print(f"I {wordle_color.RED}hate{wordle_color.ENDC} hard projects.")`

The variable `wordle_color.RED` contains the character sequence that causes the following characters to appear red. The variable `wordle_color.ENDC` contains the character sequence that returns the output to normal.

(If you are curious, these "special character sequences" are [ANSI escape codes](https://saturncloud.io/blog/how-to-print-colored-text-to-the-terminal/).)

## Instructions

**Step 1:** Begin by examining the function `wordle_engine.welcome_string()` to see how to use colors.
Practice using the `wordle_colors` class by adding a line or two to the welcome message. (You may [add additional colors](https://gist.github.com/JBlond/2fea43a3049b38287e5e9cefc87b2124) to the class if you like; but, you must follow the specifications when displaying guesses and letter options.)

**Step 2:** Implement and use functions in `wordle_engine.py` as documented. Don't give them different behavior, and don't modify their parameters or return values.

**Step 5:** Now, write the main game loop in `wordle.py`. 

You must implement the code in `wordle_engine.py` so that it passes the instructor's tests. Also, your game must do the following:
   * Reject guesses that are not exactly 5 letters
   * Reject guesses that are not valid words
   * Limit players to 6 guesses
   * Display the entire history of guesses before each prompt.
   * Print a message at the end of the game indicating whether the player won or lost.
      * If the player wins, display the entire sequence of guesses as part of the final message.

Other than that, you have freedom to design the game how you like.

The starter code comes with two files
* `combined_wordlist.txt`  This is the set of all acceptable guesses.
* `shuffled_real_wordles.txt` This much shorter list is the set of potential "target" words.

The target word is chosen in one of two ways:
  1. Specify it on the command line
  2. Choose it randomly from the list of all acceptable guesses (You must add code to implement this.)

Instead of choosing the target from the list of all words, you can choose it randomly from  `shuffled_real_wordles.txt`. (This option requires a little extra work (and extra points) on your part to open and load this extra file.)  

**IMPORTANT:** Be sure to test your entire program thoroughly.  Automated tests cover only a small portion of this assignment. Simply passing the automated tests does _not_ mean that your project is complete.


Example Scenrios to test:

```
Scenario: 
    User makes a sequence of guesses and wins the game in four steps:
Input Sequence:
    audio
    stern
    glyph
    audit
Watch for:
    Message indicating that the user wins the game.    

Scenario:
    User enters words that have fewer than 5 letters
Input Sequence:
    audio
    safe
    step
    stop
    stomp
Watch For:
    Error message indicating required word length.
    Ability to continue game after entering 5 letter word
```