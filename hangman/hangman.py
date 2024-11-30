import os
import json
import random

# ASCII art for Hangman stages
HANGMAN_STAGES = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
]

def load_words():
    """Load words from a JSON file."""
    print("Current working directory:", os.getcwd())

    try:
        with open('words.json', 'r') as file:
            data = json.load(file)
            return data.get('words', [])
    except FileNotFoundError:
        print("Error: 'words.json' not found.")
        return []
    except json.JSONDecodeError:
        print("Error: JSON file is not properly formatted.")
        return []

def hangman():
    words = load_words()
    if not words:
        print("No words available to play. Please check your JSON file.")
        return

    word = random.choice(words)  # Randomly select a word
    guessed_word = ['_'] * len(word)  # Placeholder for the word
    guessed_letters = set()  # Set to track guessed letters
    attempts = 6  # Number of attempts

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")

    while attempts > 0 and '_' in guessed_word:
        # Display the current hangman stage
        print(HANGMAN_STAGES[6 - attempts])

        # Display the current word and guessed letters
        print("Current word:", ' '.join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            attempts -= 1

    # Game result
    if '_' not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print(HANGMAN_STAGES[0])  # Display the full hangman
        print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()
