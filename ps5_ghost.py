# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!

WORD_LENGTH = 3

def is_valid_letter(letter):
    """
    Returns True if the input letter contains only one character
    in ascii_letters. Both upper and lower case is OK. Otherwise
    returns False.
    :param letter: string
    :return: True or False
    """
    if len(letter) != 1:
        return False
    if letter not in string.ascii_letters:
        return False
    return True

# def test_is_valid_letter():
#     test_set = ['a', 'd', 'A', 'X', '%', '4', '', 'ab']
#     test_value_set = [1,1,1,1,0,0,0,0]
#     failure = False
#     for letter,value in zip(test_set,test_value_set):
#         if is_valid_letter(letter) != value:
#             print 'FAILURE: test_is_valid_letter()'
#             print "\tExpected {}, but got {} for letter: '{}'".format(value,is_valid_letter(letter),letter)
#             failure = True
#     if not failure:
#         print "SUCCESS: test_is_valid_letter()"

# test_is_valid_letter()

def get_letter(pn):
    """
    Ask the pn th player(user) to input a letter, and check the input
    to see wether it's valid. Return the value of the letter until it
    gets a valid one.
    :param pn: Integer represents the current player number.
    :return: Single letter string
    """
    while True:
        letter = raw_input('Player {} says letter: '.format(pn)).upper()
        if is_valid_letter(letter):
            return letter
        else:
            print 'Invalid input, try again.'

def initializeGhost():
    """
    Initialize the program, ask for the first input.
    :return: a string which is the first character
    """
    word_fragment = ''
    print 'Welcome to Ghost!'
    print 'Player 1 goes first.'
    print "Current word fragment: '" + word_fragment +"'"
    word_fragment += get_letter(1)
    return word_fragment

# print initializeGhost()

def deal_fragment(word_fragment,playerNum,n):
    """
    Deal with the current word_fragment entered by current player playerNum,
    n is to indicate the limit: when the length of the word fragment greater
    than n, the function should check if the fragment is a word in the word list.
    Checks the word_fragment to see if one lose the game.
    :param word_fragment: String, current word fragment
    :param playerNum: Integer, the current player number
    :param n: Integer
    :return: True or False
    """
    if len(word_fragment) > n and word_fragment.lower() in wordlist:
        print "Player {} loses because '{}' is a word!".format(playerNum,word_fragment)
        print "Player {} wins!".format((playerNum+2)%2 + 1)
        return False
    for word in wordlist:
        if word.find(word_fragment.lower()) == 0:
            return True
    print "Player {} loses because no word begins with '{}'!".format(playerNum,word_fragment)
    print "Player {} wins!".format((playerNum+2)%2 + 1)
    return False

def ghost():
    """
    The main function of the word game "ghost".
    :return: None
    """
    word_fragment = initializeGhost()
    playerNum = 1
    while True:
        print "\nCurrent word fragment: '{}'".format(word_fragment)
        is_valid_fragment = deal_fragment(word_fragment,playerNum,WORD_LENGTH)
        if not is_valid_fragment:
            break
        playerNum = (playerNum+2) % 2 + 1
        print "Player {}'s turn.".format(playerNum)
        letter = get_letter(playerNum)
        word_fragment += letter


if __name__ == "__main__":
    ghost()




