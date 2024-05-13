# Hangman Game

This Hangman game is a simple command-line game written in Python. The player tries to guess a secret word by suggesting letters within a certain number of tries.

## Features

- Interactive guessing of letters.
- Display of ASCII art for each wrong guess to visually represent the hangman.

## How to Play
1. Start the game by running the main.py file:
2. When prompted, enter the path to a text file containing words, one per line.
3. Enter the index of the word you want to guess (e.g., 1 for the first word).
4. Start guessing letters to try and reveal the secret word.
5. You are allowed up to 6 incorrect guesses before the game ends.

## Game Rules
- The game picks a word at random from a provided text file based on the given index.
- The player suggests letters one at a time.
- Each incorrect guess results in a part of the hangman being drawn.
- The game continues until the player either guesses the word correctly or exhausts all allowed tries.
