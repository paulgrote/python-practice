hand1 = ['1','3','4','8']
hand2 = ['7','8','9']
hand3 = ['2']
hand4 = ['3','5','7']

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

print('HAND 1')
print(check_for_win(hand1))

print('\nHAND 2')
print(check_for_win(hand2))

print('\nHAND 3')
print(check_for_win(hand3))

print('\nHAND 4')
print(check_for_win(hand4))