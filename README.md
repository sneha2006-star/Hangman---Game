# Hangman Game in Python

## Project Description

The Hangman Game is a simple, text-based word-guessing game developed using Python. The player has to guess a hidden word one letter at a time. The game selects a random word from a list of five predefined words.

The player gets a maximum of 6 incorrect guesses to find the correct word. The game ends when the player guesses the word correctly or runs out of attempts.

## Features

* Random word selection.
* Five predefined words.
* Maximum of 6 incorrect guesses.
* Letter-by-letter word guessing.
* Input validation to ensure the player enters a single letter.
* Detection of repeated guesses.
* Displays the remaining incorrect guesses.
* Shows the correct word when the game ends.

## Technologies Used

* Python
* Random module
* While loop
* If-else statements
* Lists and strings
* User input and output

## How to Run the Project

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Clone the Repository

```bash
git clone <your-repository-link>
```

### Step 3: Open the Project Folder

```bash
cd hangman-game
```

### Step 4: Run the Program

Save the code in a file named `hangman.py` and execute:

```bash
python hangman.py
```

## Sample Output

```text
===== HANGMAN GAME =====
Guess the word one letter at a time!
You have 6 incorrect guesses.

Word: _ _ _ _ _
Incorrect guesses left: 6
Enter a letter: a
Correct guess!

Word: a _ _ _ _
Incorrect guesses left: 6
Enter a letter: p
Correct guess!

Congratulations! You guessed the word: apple
```

*Note: The actual word and game output may vary because the word is selected randomly.*

## Learning Outcomes

Through this project, I learned how to:

* Use Python's random module to select a word.
* Work with lists and strings.
* Apply loops and conditional statements.
* Take input from the user.
* Validate user input.
* Implement a simple game using programming logic.

## Future Improvements

* Add more words to the word list.
* Display a visual Hangman.
* Add difficulty levels.
* Allow the player to play multiple rounds.
* Track the player's score.

