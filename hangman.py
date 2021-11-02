MAX_TRIES = 6
HANGMAN_ASCII_ART = """
 _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/\n"""


def hangman_welcome_opening():
    """
    prints to player the opening screen of the game
    :return: nothing just prints
    :rtype: None
    """
    print(HANGMAN_ASCII_ART, MAX_TRIES)


def check_valid_input(guess_letter, old_letters_guessed):
    """
    checks if input user just typed in is correct by number of limitations
    :param guess_letter: contains what user just typed in
    :param old_letters_guessed: list of letters got by user before
    :type guess_letter: str
    :type: old_letters_guessed: list
    :return: if what got by the user is correct or not
    :rtype: boolean
    """
    if len(guess_letter) > 1 or not (guess_letter.isalpha()) or guess_letter in old_letters_guessed:
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    """
    try to update the char the user just has typed
    :param letter_guessed: char user just has typed
    :type letter_guessed: str
    :param old_letter_guessed: list of chars already typed in
    :type old_letter_guessed: list
    :return: if update gone well or not
    :rtype: boolean
    """
    if check_valid_input(letter_guessed, old_letter_guessed):
        old_letter_guessed.append(letter_guessed)
        return True

    print('X')
    print_old_letter_guessed(old_letter_guessed)
    return False


def print_old_letter_guessed(old_letter_guessed):
    """
    print the list of the chars typed by the user
    :param old_letter_guessed: list of chars entered by user
    :type old_letter_guessed: list
    :return: just printing
    :rtype: None
    """
    print(" -> ".join(sorted(old_letter_guessed, key=str.lower)))


def show_hidden_word(secret_word, old_letter_guessed):
    """
    shows to user the word he needs to guess in a way that the chars of the word he already guessed
    correctly are presented in place and the rest is represented by _ (underline)
    :param secret_word: the word user needs to guess
    :type secret_word: str
    :param old_letter_guessed: includes letters user typed
    :type old_letter_guessed: list
    :return: whole word with _ for chars he didn't guess
    :rtype: str
    """
    my_str = ""
    for char in secret_word:
        if char in old_letter_guessed:
            my_str += char
            my_str += " "
        else:
            my_str += "_ "
    return my_str


def check_win(secret_word, old_letter_guessed):
    """
    check if player succeeded to guess the word
    :param secret_word: word player needs to guess
    :type secret_word: str
    :param old_letter_guessed: chars typed by user
    :type old_letter_guessed: list
    :return: if succeeded or not
    :rtype: bool
    """
    for ch in secret_word:
        if ch not in old_letter_guessed:
            return False
    return True


# dict that holds all the stages of hangman as values and keys are from 0 to 6
HANGMAN_PHOTOS = \
    {0: 'x-------x',
     1: """
    x-------x
    |
    |
    |
    |
    |
    """,
     2: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
     3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
     4: """
     x-------x
     |       |
     |       0
     |      /|\ 
     |
     |
     """,
     5: """
     x-------x
     |       |
     |       0
     |      /|\ 
     |      /
     |
    """,
     6: """
      x-------x
      |       |
      |       0
      |      /|\ 
      |      / \ 
      |
      """}


def print_hangman(num_of_tries):
    """
    prints the stages of the hangman depends on number of wrong guesses
    player did
    :param num_of_tries: number of wrong guesses player did
    :type num_of_tries: int
    :return: nothing just prints on screen
    :rtype: None
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    """
        reads from file of words a word to be used as the word the user needs to guess
        :param file_path: path to the file of words
        :param index: points to a specific word
        :type file_path: str
        :type index: str (as long as it come from input of user)
        :return: a single word for the game
        :rtype: str
        """

    with open(file_path, 'r') as input_file:
        words = input_file.read()
        words_list = words.split(' ')
        return words_list[(int(index) - 1) % len(words_list)]


def main():
    hangman_welcome_opening()
    file_path = input("Enter file path: ")
    index = input("Enter index: ")
    print("\nLet's start!\n")
    print("\t" + HANGMAN_PHOTOS[0])
    secret_word = choose_word(file_path, index)
    old_letters_guessed = []
    num_of_tries = 0  # keeps track of number of failed guesses
    print(show_hidden_word(secret_word, old_letters_guessed) + "\n")

    while True:
        guess_letter = input("Guess a letter: ")
        # if input not valid keeps asking input from user until input is valid
        while not try_update_letter_guessed(guess_letter, old_letters_guessed):
            guess_letter = input("Guess a letter: ")

        # in case of failed guess
        if guess_letter not in secret_word:
            print(':(' + '\n' + HANGMAN_PHOTOS[num_of_tries + 1])
            num_of_tries += 1
        # in all cases
        print(show_hidden_word(secret_word, old_letters_guessed))

        if num_of_tries == MAX_TRIES:  # if user made failed guesses in the number
            # specified from start then he loses and game terminates
            print('LOSE')
            return

        if check_win(secret_word, old_letters_guessed):
            print('WIN')
            return


if __name__ == '__main__':
    main()
