# Hangman App Outline

## Variables

- lives = the amount of lives or guesses user has left
- chosenWord = the chosen word either from (see below) list of possible words or randomly generated word
- usedLetters = empty to begin with, will become a list with users guesses as user guesses

## Data Structures

- List: of possible words OR randomly generate a word based on OS time within set parameters
- List: of letters that user has guessed
- List: of possible hangman variations - will need to user ascii art to draw a hangman

## Functions

- function to take user input
  - loop to keep asking for input if the user input is invalid. ex: a number, multiple letters, nothing. Can convert toUpper or toLower so user can input either without error
  - needs to add valid guesses to the list of letters user guessed
- function to display the users guessed letters
- function to loop the the letter in theWord and display the letter if it matches a letter in theWord
- function to display the hangman graphics
- function to display guessing interface
- intro/start screen
  - title
  - simple rule explanation
  - press any key to begin
- check if the player has won or lost
  - if player runs out of lives/guesses - lose
  - if player correctly guesses the word - win
