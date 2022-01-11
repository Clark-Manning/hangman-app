from random_word import RandomWords

r = RandomWords()
INITIAL_LIVES = 6

# RandomWords package has an issue where it returns None sometimes. 
def get_random_word(min=4, max=10):
    return r.get_random_word(minLength=min, maxLength=max).lower()
 
def get_word_progess(chosen_word, lives, word_progress=[], user_guess=None):
    len_chosen_word = len(chosen_word)
    lose_life = True
    for i in range(len_chosen_word):
        current_character = chosen_word[i]
        if user_guess == current_character:
            word_progress[i] = user_guess
            lose_life = False
    if lose_life == True:
        lives -= 1
    return word_progress, lives

def display_word_progress(word_progress):
    print(" ".join(word_progress))

# assimiliate into get_word_progress() so as not to duplicate code
def store_user_guess(chosen_word, stored_guesses, user_guess):
    len_chosen_word = len(chosen_word)
    add_guess = True
    for i in range(len_chosen_word):
        current_character = chosen_word[i]
        if user_guess == current_character:
            add_guess = False
    if add_guess == True:
        stored_guesses.append(user_guess)
    return stored_guesses

def display_user_guesses(stored_guesses):
    print("Current missed guesses: " + (" ".join(stored_guesses)))

def get_user_input(user_input_list):
    while True:
        user_input = input("Please enter a letter: ").lower()
        if user_input == "":
            print("Sorry, you did not provide an answer.")
        elif not user_input.isalpha():
            print("Sorry, your answer was not a letter.")
        elif len(user_input) >= 2:
            print("Please enter only a single letter.")
        elif user_input in user_input_list:
            print("You already entered that letter, try again.")
        else:
            user_input_list.append(user_input)
            return user_input, user_input_list
    

def play_game():
    chosen_word = get_random_word()

    # flag for when I want to print the chosen_word before the game starts, i.e for tests
    test_chosen_word = True
    if test_chosen_word == True:
        print(chosen_word)

    lives = INITIAL_LIVES
    stored_guesses = []
    user_input_list = [] 

    len_chosen_word = len(chosen_word)
    word_progress = ["_"] * len_chosen_word
    display_word_progress(word_progress)

    while lives > 0 and ("_" in word_progress):
        print("You have " + str(lives) + " lives left.")
        user_guess, user_input_list = get_user_input(user_input_list)
        word_progress, lives = get_word_progess(chosen_word, lives, word_progress, user_guess)
        display_word_progress(word_progress)
        stored_guesses = store_user_guess(chosen_word, stored_guesses, user_guess)
        display_user_guesses(stored_guesses)

    if lives == 0:
        print("You lost! The word was '" + chosen_word + "'. Try again.")
    else:
        print("You won!")
    
if __name__ == "__main__":
    play_game()