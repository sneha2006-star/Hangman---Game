import random

# List of 5 predefined words
words = ["apple", "python", "hello", "chair", "train"]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
attempts = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while attempts > 0:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", attempts)

    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    # Take input from the player
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You have already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

else:
    print("\nGame Over! The word was:", word)
