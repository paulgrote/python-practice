from random import randint

def is_play_valid(human_play, available_spaces):
    '''
    human_play: int 
    '''
    if human_play not in available_spaces:
        print("That wasn't a valid choice. Try again: ")
        return False
    else:
        return True

def human_choice(available_spaces):
    '''
    available_spaces: list representing unplayed squares
    returns: string of a number between 1-9
    '''

    valid = False
    while valid == False:
        human_selection = input('Select a square: ')
        valid = is_play_valid(human_selection, available_spaces)

    return human_selection

def computer_choice(available_spaces):
    '''
    available_spaces: list representing unplayed squares
    returns: string of a number between 1-9
    '''
    random_index = randint(0,len(available_spaces) - 1)
    computer_selection = available_spaces[random_index]

    return computer_selection


def check_for_win(player_hand):
    '''
    player_hand: list of strings. 
    returns True if values in player hand are in winning_hands. False, otherwise.
    '''
    winning_hands = ('123','147','159','258','357','369','456','789')
    if len(player_hand) < 3:
        win = False
    else:
        for hand in winning_hands:
            if hand[0] in player_hand:
                if hand[1] in player_hand:
                    if hand[2] in player_hand:
                        win = True
                        break
            else:
                win = False

    return win

def print_board(person_squares,computer_squares):
    '''
    person_squares: list of strings
    computer_squares: list of strings
    '''
    board = []
    for i in range(1,10):
        if str(i) in person_squares:
            board.append('X')
        elif str(i) in computer_squares:
            board.append('O')
        else:
            board.append(' ')

    print(board[0],'|',board[1],'|',board[2])
    print('---------')
    print(board[3],'|',board[4],'|',board[5])
    print('---------')
    print(board[6],'|',board[7],'|',board[8])
    print('\n')


def main():
    # data
    available_spaces = ['1','2','3','4','5','6','7','8','9']
    person_choices = []
    computer_choices = []
    players = {1:'human', 2:'computer'}
    
    # randomly choose starting player (person vs computer)
    starting_player = randint(1,2)
    print(players[starting_player].title(), 'starts!')

    # game loop
    for turn in range(starting_player,starting_player + 9):

        if turn % 2 != 0:
            choice = str(human_choice(available_spaces))
            person_choices.append(choice)
            available_spaces.remove(choice)
            print_board(person_choices,computer_choices)
            if check_for_win(person_choices) == True:
                print('You win!')
                break


        else:
            choice = str(computer_choice(available_spaces))
            print('Computer choice:',choice)
            computer_choices.append(choice)
            available_spaces.remove(choice)
            print_board(person_choices,computer_choices)
            if check_for_win(computer_choices) == True:
                print('Computer wins :(')
                break

main()