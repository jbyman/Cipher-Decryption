import sys
import string

#
# Constants
#

STANDARD_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
                     'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

STANDARD_ALPHABET_FREQUENCIES = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U',
                     'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']


#
# Helper functions
#

def get_text_data(filename):
    """
    Given a filename, return the contents of the file

    @param filename is the name of the text file
    @returns the file in string form
    """

    with open(filename, 'rb') as data:
        res = data.read()
    return bytes.decode(res.upper())


def get_frequency_dict(string):
    """
    Iterate over the ciphertext and determine the frequency of each letter

    @param string is the ciphertext
    @returns a dictionary of letter:frequency
    """

    used_letters = []
    letter_dict = {}
    total_num_words = 0.0
    for letter in string:
        if letter == " " or letter == '\n':
            continue
        total_num_words += 1
        if letter not in used_letters:
            letter_dict[letter] = 1
            used_letters.append(letter)
        else:
            letter_dict[letter] += 1

    for i in letter_dict.keys():
        letter_dict[i] /= total_num_words
    for elem in missing_letters(as_list(letter_dict)):
        letter_dict[elem] = 0
    return letter_dict


def as_list(tup_list):
    """
    Turns a tuple-list into a list of the first element of the tuple

    @param tup_list is the tuple-list you are converting
    @returns the created list
    """

    res = []
    for elem in tup_list:
        res.append(elem[0])
    return res


def list_to_string(l):
    """
    Converts a string list in to a string

    @param l is the string list
    @returns a concatentation of each element in the list
    """

    res = ""
    for elem in l:
        res += elem
    return res


def english_words_percentage(string):
    """
    Given a string, returns the percentage of words that are English words

    @param string is the string you are analysing for proportions
    @param all_english_words is the list of all valid english words
    @returns a float from 0 to 1 representing the percentage
    """

    all_english_words = get_text_data("dictionary.txt")

    total_num_words = len(string.split(" "))
    num_english_words = 0.0
    all_english_words = all_english_words.split("\n")
    all_english_words = set(all_english_words)

    for word in string.split(" "):
        if word in all_english_words:
            num_english_words += 1
    return num_english_words / total_num_words


def missing_letters(alphabet):
    """
    Given a list, return the missing letters of the alphabet

    @param alphabet is the list of letters you are comparing to the alphabet
    @returns a list of missing letters
    """

    res = []
    for letter in list(string.ascii_uppercase):
        if letter not in alphabet:
            res += letter
    return res


def index_of_spaces(text):
    """
    Given text, return all space indices

    @param text is the string to analyze
    @returns a list of integers representing the indices
    """

    res = []
    for i in range(0, len(text)):
        if text[i] == ' ':
            res.append(i)
    return res


def next_letter(letter):
    """
    Helper function to get the next letter
    after a letter.

    Example: next_letter('A') -> B,

    @param letter is the letter you are starting with
    @returns letter + 1 in the alphabet
    """

    res = ''

    if ord(letter) < 65:
        res = 'Z'
    elif ord(letter) >= 90:
        res = 'A'
    else:
        res = chr(ord(letter) + 1)

    return res


def get_args():
    """
    Return all CLI arguments
    """

    args = {}

    args['CIPHER'] = sys.argv[2].upper()
    args['SHOULD_ENCRYPT'] = (sys.argv[1].upper() == 'ENCRYPT')
    if args['SHOULD_ENCRYPT']:
        args['ENCRYPTION_KEY'] = sys.argv[4]
        args['FILENAME'] = sys.argv[3]
    else:
        args['FILENAME'] = sys.argv[3]
        args['SHOULD_DECRYPT'] = True
        if args['CIPHER'] == 'VIGENERE':
            args['VIGENERE_KEY_LENGTH'] = sys.argv[4]

    return args


def add_letters(letter1, letter2):
    """
    Helper function to add two letters together
    """

    increment = ord(letter2) % 65
    ascii_value = ord(letter1) + increment

    if ascii_value > 90:
        ascii_value = ascii_value - 26

    if ascii_value < 65:
        ascii_value += 26

    if ascii_value < 65 or ascii_value > 90:
        print("ERROR ADDING" + letter1 + " AND " + letter2)
        import sys
        sys.exit()

    return chr(ascii_value)


def subtract_letters(letter1, letter2):
    """
    Helper function to subtract letter2 from letter1
    """

    increment = ord(letter2) % 65
    ascii_value = ord(letter1) - increment

    if ascii_value > 90:
        ascii_value = ascii_value - 26

    if ascii_value < 65:
        ascii_value += 26

    if ascii_value < 65 or ascii_value > 90:
        print("ERROR SUBTRACTING " + letter1 + " AND " + letter2)
        import sys
        sys.exit()

    return chr(ascii_value)
