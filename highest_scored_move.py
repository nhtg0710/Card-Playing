from score import score
from N_of_a_kind import possible_n as n
from run import rec_card
def highest(hand):
    '''take a list as an argument, return the move with highest score if any'''
    play = []
    for group in n(hand):
        play.append(group)
    for card in hand:
        if len(rec_card(hand, card)) >= 3:
            play.append(rec_card(hand, card)[-6:])
    play = sorted(play, key=lambda x: score(x), reverse=True)
    if play:
        return play[0]
    else:
        return play
    
def highest_possible_move(hand):
    '''take a list of card as an argument, return a list with length of 3
    worth the most score, if any'''
    play = []
    for group in n(hand):
        if len(group) == 3:
            play.append(group)
    for card in hand:
        if len(rec_card(hand, card)) >= 3:
            play.append(rec_card(hand, card)[-3:])
    play = sorted(play, key=lambda x: score(x), reverse=True)
    if play:
        return play[0]
    else: 
        return play