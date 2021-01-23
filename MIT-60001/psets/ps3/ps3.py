# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*':0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    word_length = len(word)
    word = word.lower()
    letters_sum = 0
    

    for letter in word:
        letters_sum = letters_sum + SCRABBLE_LETTER_VALUES[letter]

    hand_value = 7 * word_length - 3 * (n - word_length)

    if hand_value < 1:
        word_score = letters_sum * 1
    else:
        word_score = letters_sum * hand_value

    return word_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    vowels_in_hand = []

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    for key in hand.keys():
        if key in VOWELS:
            vowels_in_hand.append(key)
 
    y = random.choice(vowels_in_hand)
    if hand[y] > 1:
        hand[y] = hand.get(y) - 1
        hand['*'] = 1
    else:
        hand['*'] = hand.pop(y)

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_hand = hand.copy()

    for letter in word.lower():
        if letter in updated_hand.keys():
            updated_hand[letter] -= 1
    
    for key,value in dict(updated_hand).items():
        if value <=0:
            del updated_hand[key]

    return updated_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    if '*' in word:
        for vowel in VOWELS:
            test_word = word
            test_word = test_word.replace('*', vowel)
            if test_word.lower() in word_list:
                valid_word = True
                break
            else:
                valid_word = False
    elif word.lower() in word_list:
        valid_word = True
    else:
        valid_word = False
    
    word_dict = get_frequency_dict(word.lower())

    for key, value in word_dict.items():
        if key not in hand.keys():
            valid_dict = False
            break
        elif value > hand[key]:
            valid_dict = False
            break 
        else:
            valid_dict = True
    
    if valid_word == True and valid_dict == True:
        valid = True
    else:
        valid = False

    return valid

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    num_letters = hand.values()
    handlen = sum(num_letters)

    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        print('Current Hand:', end='')
        display_hand(hand)
        # Ask user for input
        user_word = input('Enter word, or "!!" to indicate you are finished: ')
        # If the input is two exclamation points:
        if user_word == '!!':
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_word, hand, word_list) == True:
                # Tell the user how many points the word earned,
                # and the updated total score
                total_score = total_score + get_word_score(user_word, calculate_handlen(hand))
                print('"%s" earned %i points. Total: %i points.' % (user_word, get_word_score(user_word, calculate_handlen(hand)), total_score))
            else:
            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, user_word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score [don't need to do this when play_game is used]
    # print('Total score: %i points.' % total_score)
    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    if letter in hand.keys():
        available_letters =  VOWELS + CONSONANTS
        for key in hand:
            available_letters = available_letters.replace(key,'')
        new_letter = random.choice(available_letters)
        new_hand[new_letter] = new_hand.pop(letter)

    return new_hand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    number_hands = int(input("Enter the total number of hands: "))
    final_score = 0
    substitute_count = 1
    replay_count = 1

    while number_hands > 0:
        current_hand = deal_hand(HAND_SIZE)
        if substitute_count > 0:
            # print current hand
            print('Current Hand: ', end='')
            display_hand(current_hand)
            # ask if they want to substitute a letter
            substitute = input('Would you like to substitute a letter? (yes/no) ')
            # if yes, prompt for letter, then update hand and decrement substitute_count
            if substitute == 'yes':
                letter = input('Which letter would you like to replace? ')
                current_hand = substitute_hand(current_hand, letter)
                substitute_count -= 1
        
        hand_score1 = play_hand(current_hand, word_list)
        print('Total score for this hand:', hand_score1)
        print('--------------------------')

        hand_score2 = 0
        if replay_count > 0:
            # ask if they want to play the hand again
            replay = input('Would you like to replay the hand? (yes/no) ')
            if replay == 'yes':
                hand_score2 = play_hand(current_hand, word_list) 
                print('Total score for this hand:', hand_score2)
                print('--------------------------')
                replay_count -= 1
        
        if hand_score2 > hand_score1:
            highest_score = hand_score2
        else:
            highest_score = hand_score1

        final_score = final_score + highest_score
        number_hands -= 1
    
    print('Total score for all hands:',final_score)
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
