from score import score
from N_of_a_kind import possible_n as n
from valid_table import valid_table as vt
from run import rec_card
from highest_scored_move import highest
from highest_scored_move import highest_possible_move
play = []  # the list of playable cards
opens = False
def comp10001huxxy_bonus_play(play_history, active_player, hand, table):   
    # we want to count how many moves our player has made
    count = 0
    for move in play_history[::-1]:
        if move[0] != active_player:
            break
        count += 1
    if count == 6:  # if player already played 6 turns
        return active_player, 3, None
    elif count == 0:
        global play
        play = highest(hand)
        # now that play is only a list of the highest-scored move possible,
        # need to find a new way around play
        global opens
        if not opens:  # if haven't opened yet
            if not play:  # if there's nothing playable
                return active_player, 0, None
            if play:  # if there is something playable
                if 'XX' in hand and 'XX' not in play:
                    play.append('XX')
                if score(play[:3]) >= 24:
                    opens = True  
                    return active_player, 1, (play.pop(0), len(table))
                else:
                    return active_player, 0, None
            else:
                return active_player, 0, None
        if opens:  # if a player has played opening turn
            if play:  
                return active_player, 1, (play.pop(0), len(table))
            
            # find playable groups in current hand, 
            # if previous groups are exhausted and there's nothing left
            if not play:                  
                play = highest(hand)  
                if play:
                    if 'XX' in hand and 'XX' not in play:
                        play.append('XX')
                    return active_player, 1, (play.pop(0), len(table))
                elif not play:  
                    found = False
                    for group in table:
                        for card in hand:
                            if card == 'XX':
                                a = card
                                if a not in group and len(group) < 8:
                                    index = table.index(group)
                                    found = True
                                    break
                            elif vt([group + [card]]):
                                index = table.index(group)
                                a = card
                                hand.remove(card)
                                found = True
                                break
                    if found:  # if got the card, play that card
                        return active_player, 1, (a, index)
                    else:
                        return active_player, 0, None
    elif count > 0:
        if play:
            return active_player, 1, (play.pop(0), len(table) - 1)
        elif not play:
            if count <= 3:
                play = highest_possible_move(hand)
                if play:
                    return active_player, 1, (play.pop(0), len(table))
                
                # take the cards that don't form any group with one another
                # try if they can go in any group in the current table 
                else:
                    found = False
                    for group in table:
                        for card in hand:
                            if card == 'XX':
                                a = card
                                if a not in group and len(group) < 8:
                                    index = table.index(group)
                                    found = True
                                    break
                            elif vt([group + [card]]):
                                index = table.index(group)
                                a = card
                                hand.remove(card)
                                found = True
                                break
                    if found:
                        return active_player, 1, (a, index)
                    else:
                        return active_player, 3, None
            
            # take the cards that don't form any group with one another
            # try if they can go in any group in current table 
            elif count > 3: 
                found = False
                for group in table:
                    for card in hand:
                        if vt([group + [card]]):
                            index = table.index(group)
                            a = card
                            hand.remove(card)
                            found = True
                            break
                if found:
                    return active_player, 1, (a, index)
                else:
                    return active_player, 3, None