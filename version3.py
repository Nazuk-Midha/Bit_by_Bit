import random

def display_hangman(wrong_guesses):
    stages = [
        # head, torso, both arms, both legs
        """
            --------
            |      |h
           |      O
           |     /|\\
           |     / \\
           |
           |
          ----
        """,
        # head, torso, both arms, one leg
        """
            --------
            |      |
            |      O
            |     /|\\
            |     /
            |
            |
          ----
        """,
        # head, torso, both arms
        """
            --------
            |      |
            |      O
            |     /|\\
            |
            |
            |
          ----
        """,
        # head, torso, one arm
        """
            --------
            |      |
            |      O
            |     /|
            |     /
            |
            |
          ----
        """,
        # head, torso
        """
            --------
            |      |
            |      O
            |     /|
            |     /
            |
            |
          ----
        """,
        # head
        """
            --------
            |      |
            |      O
            |     /|\\
            |     /
            |
            |
          ----
        """,
        # empty
        """
            --------
            |      |
            |
            |
            |
            |
            |
          ----
        """
    ]
    print(stages[wrong_guesses])

def get_word():
    words = ["python", "programming", "computer", "game", "hangman"]
    return random.choice(words)

def display_instructions():
    print("\033[1mWelcome to Hangman!\033[0m")
    print("Instructions:")
    print("1. Player 1 will enter a word.")
    print("2. Player 2 will guess the letters of the word.")
    print("3. Player 2 will have 6 chances to guess the word correctly.")
    print("Let's start!\n")

def play():
    display_instructions()

    word = input("\033[1mPlayer 1, enter a word: \033[0m").lower()
    while not word.isalpha():
        word = input("\033[1mPlease enter a valid word: \033[0m").lower()

    word_letters = set(word)  # Letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # Letters used by the player
    wrong_guesses = 0

    while len(word_letters) > 0 and wrong_guesses < 6:
        # Display current guess with underscores
        print("\nCurrent guess: ", end=' ')
        for letter in word:
            if letter in used_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

        # Get user input
        while True:
            user_letter = input("\033[1mPlayer 2, guess a letter: \033[0m").lower()
            if len(user_letter) != 1 or user_letter not in alphabet - used_letters:
                print("\033[1mInvalid input. Please enter a single unused letter.\033[0m")
            else:
                break
        used_letters.add(user_letter)

        # Check if the guess is correct
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            wrong_guesses += 1
            display_hangman(wrong_guesses)

    # End game message
    if wrong_guesses < 6:
        print("\033[92m\nCongratulations! Player 2 guessed the word '%s' correctly.\033[0m" % word)
    else:
        print("\033[91m\nPlayer 2 ran out of guesses. The word was: %s\033[0m" % word)

if __name__ == "__main__":
    play()
