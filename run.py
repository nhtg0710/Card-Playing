def next_card(hand, card): 
    '''take a list of cards and a card as arguments, return one next
    card that would make a valid run with the original card, given that
    the suggested card is in the original hand'''
    dic = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13, 'X': 1000}
    rdic = {value: key for key, value in dic.items()}
    pos_card = []
    if card[1] in 'SC' and dic[card[0]] != 13:  # can't be the Kings
        pos_card.append(rdic[dic[card[0]] + 1] + 'D')
        pos_card.append(rdic[dic[card[0]] + 1] + 'H')
    elif card[1] in 'DH' and dic[card[0]] != 13:
        pos_card.append(rdic[dic[card[0]] + 1] + 'S')
        pos_card.append(rdic[dic[card[0]] + 1] + 'C')
    list0 = []
    for i in pos_card:
        if i in hand:
            list0.append(i)
    return list0
def rec_card(hand, card):
    '''take a list of cards and a card as arguments, return a run that can be
    made using cards from the given hand and contains the given card'''
    nextcards = next_card(hand, card)
    if not nextcards:
        return [card]
    else:
        for i in nextcards:
            return [card] + rec_card(hand[1:], i)