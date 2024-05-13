# constant that defines the maximum number of incorrect guesses the player is allowed before losing the game.
MAX_TRIES = 6

# string of ASCII art that is displayed at the beginning of the game.
HANGMAN_ASCII_ART = r"""Welcome to the game Hangman
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/"""

# dictionary that maps the number of incorrect guesses to the corresponding Hangman ASCII art.
HANGMAN_PHOTOS = {
    "0":
        """
        x-------x
        """
    , "1":
        """
        x-------x
        |
        |
        |
        |
        |
        """
    , "2":
        """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
    "3":
        """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,
    "4":
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
    "5":
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """,
    "6":
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """}