import random

def display_hangman(wrong_guesses):
  stages = [
      #  head, torso, both arms, both legs
      """
          --------
          |      |
          |
          |
          |
          |
          |
         ----
      """,
      #  head, torso, both arms, one leg
      """
          --------
          |      |
          |      O
          |
          |
          |
          |
         ----
      """,
      #  head, torso, both arms
      """
          --------
          |      |
          |      O
          |     /|\
          |
          |
          |
         ----
      """,
      #  head, torso, one arm
      """
          --------
          |      |
          |      O
          |     /|\
          |     /
          |
          |
         ----
      """,
      #  head, torso
      """
          --------
          |      |
          |      O
          |     /|\
          |     / \
          |
          |
         ----
      """,
      #  head
      """
          --------
          |      |
          |      O
          |     /|\
          |     /
          |
          |
         ----
      """,
      #  empty
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

def play():
  word = get_word()
  word_letters = set(word)  # Letters in the word
  alphabet = set('abcdefghijklmnopqrstuvwxyz')
  used_letters = set()  # Letters used by the player

  wrong_guesses = 0

  while len(word_letters) > 0 and wrong_guesses < 6:
    # Display current guess with underscores
    print("Current guess: ", end=' ')
    for letter in word:
      if letter in used_letters:
        print(letter, end=' ')
      else:
        print('_', end=' ')
    print()

    # Get user input
    while True:
      user_letter = input("Guess a letter: ").lower()
      if len(user_letter) != 1 or user_letter not in alphabet - used_letters:
        print("Invalid input. Please enter a single unused letter.")
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
    print(f"Congratulations! You guessed the word {word}.")
  else:
    print("You ran out of guesses. The word was:", word)

play()
