from constant import *


def open_screen():
    print(HANGMAN_ASCII_ART, "\nThe maximum number of tries is: ", MAX_TRIES)


def check_win(secret_word, old_letters_guessed):
    """
    this function checks whether all the letters in the secret word have been guessed by the user. it returns true if all
    the letters of the secret word are in the list of old letters guessed. otherwise, it returns false.
    param secret_word: the word that the user is trying to guess.
    type secret_word: str
    param old_letters_guessed: the list of all the letters that the user has guessed.
    type old_letters_guessed: list
    return: boolean value indicating whether the user has successfully guessed all letters of the secret word.
    type: bool
    """

    # loop that iterate through each letter in the secret word to check if it has been guessed
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """"
    this function receives a secret word and a list of letters guessed by the user. it returns a string that represents
    the current state of the word being guessed, showing letters that have been correctly guessed and underscores
    for letters that have not yet been guessed.
    param secret_word: the word that the user is trying to guess.
    type secret_word: str
    param old_letters_guessed: the list of all the letters that the user guessed.
    type old_letters_guessed: list
    return: string the represent the guessed parts of the secret word and underscores for the unguessed parts.
    type: str
    """

    string = ""

    # loop that iterate through each letter in the secret word to check if it has been guessed
    for letter in secret_word:

        # checks if the letter in the secret word has been guessed
        if letter in old_letters_guessed:
            string += letter

        else:
            string += ' _ '

    return string


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    this function checks the user's guessed letter. it checks if the input is a string, if it's a
    single alphabetic character, and if it has not been guessed previously. it returns true if the guessed letter
    passes all these checks, otherwise, it returns false.
    param letter_guessed: The letter that the user has guessed.
    type letter_guessed: str
    param old_letters_guessed: a list that contain all the letters that have been guessed previously.
    type old_letters_guessed: list
    return: Boolean value indicating whether the guessed letter is valid. it returns true if the input is a single, new alphabetic character, and false otherwise.
    type: bool
    """

    # check that the guess is a string
    if type(letter_guessed) is not str:
        return False

    # check if the guess is exactly one alphabetic character
    if (len(letter_guessed) > 1) or not (letter_guessed.isalpha()):
        return False

    # check that the letter hasn't been guessed before
    if letter_guessed in old_letters_guessed:
        return False

    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    this function receives a letter guessed by the user and a list of already guessed letters and it checks if the guessed
    letter is valid by using another function and if the letter is valid, it is added to the list of guessed letters and the
    function returns true. if the letter is invalid, it prints an 'X' and the sorted list of previously guessed letters and then returns false.
    param letter_guessed: the letter to be validated and possibly added to the list.
    type letter_guessed: str
    param old_letters_guessed: the list of letters that have already been guessed.
    type old_letters_guessed: list
    return: true if the letter is a valid new alphabetic character that hasn't been guessed before, otherwise false.
    type: bool
    """

    # check if the guessed letter is valid and update the list of guessed letters if it is
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print('X')
        old_letters_guessed.sort()
        str_letters_guessed = "->".join(old_letters_guessed)
        print(str_letters_guessed)
        return False


def choose_word(file_path, index):
    """
    this function reads words from a text file and returns a word at a specified index.
    param file_path: the path to the text file that containing the words.
    type file_path: str
    param index: the index of the word to retrieve, based on 1,2,3.... if the index is greater than the number of words, it wraps around to the beginning
    type index: int
    return: the word at the specified index, adjusted for 1-based indexing and wrapping.
    type: str
    """

    # open the text file that located at the file_path for reading
    with open(file_path, 'r') as file_object:
        line = file_object.read()
        # split the string into a list of words based on spaces
        words = line.split(' ')

        # loop that reduce the index by the length of the list until it fits within the range
        while index > len(words):
            index -= len(words)

        return words[index - 1]


def main():
    # the string of the word the player needs to guess in the game.
    secret_word = ""

    # the list that stores all the letters the player has guessed.
    old_letters_guessed = []

    # counter that tracks the number of guesses the player has made.
    num_of_tries = 0

    open_screen()
    file_path = input("Please enter the path to the file ")
    index = int(input("Please enter the index of the word "))
    secret_word = choose_word(file_path, index).lower()
    print("Let's start!!!")
    print(HANGMAN_PHOTOS[str(num_of_tries)])
    print(show_hidden_word(secret_word, old_letters_guessed))

    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        boolean = False
        current_letter = ""

        while not boolean:
            current_letter = input("Guess a letter ").lower()
            boolean = try_update_letter_guessed(current_letter, old_letters_guessed)

        if current_letter not in secret_word:
            num_of_tries += 1
            print("):\n", HANGMAN_PHOTOS[str(num_of_tries)])

        print(show_hidden_word(secret_word, old_letters_guessed))

    if check_win(secret_word, old_letters_guessed):
        print("WIN :)")

    else:
        print("LOSE :(")


if __name__ == "__main__":
    main()
