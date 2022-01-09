from random_word import RandomWords

# TODO: store guessed letters and display
# TODO: make sure user doesn't add invalid chars or something they have already guessed

r = RandomWords()
INITIAL_LIVES = 6

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

# need case for when user enters too many characters
def get_user_input():
    while True:
        user_input = input("Please enter a letter: ").lower()
        if user_input == "":
            print("Sorry, you did not provide an answer.")
        elif not user_input.isalpha():
            print("Sorry, your answer was not a letter")

def play_game():
    chosen_word = get_random_word()
    print(chosen_word)
    lives = INITIAL_LIVES

    len_chosen_word = len(chosen_word)
    word_progress = ["_"] * len_chosen_word
    display_word_progress(word_progress)

    while lives > 0 and ("_" in word_progress):
        print("You have " + str(lives) + " lives left.")
        user_guess = input("Please enter a single letter: ").lower()
        word_progress, lives = get_word_progess(chosen_word, lives, word_progress, user_guess)
        display_word_progress(word_progress)
    
    
if __name__ == "__main__":
    get_user_input()