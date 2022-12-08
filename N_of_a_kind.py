from valid_table import valid_table as vt
from score import score
from collections import defaultdict as dd
def possible_n(hand):
    '''take a list of cards as an argument, return a list of possible 
    N-of-a-kinds, sorted by their scores from high to low'''
    dic = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}
    d1 = dd(list)  # dictionary of possible N of a kind
    # try to see if can form any N of a kind:
    if 'XX' in hand:
        hand.remove('XX')
        if 'XX' in hand:
            hand.remove('XX')
    for card in hand:
        for num, value in dic.items():
            if value == dic[card[0]]:
                d1[num].append(card)
    list1 = []
    for group in d1.values():
        if len(group) > 6:
            group = group[:6]  # just take the group with highest score
        if len(group) < 3:
            continue
        if len(group) == 3:
            if vt([group]):
                list1.append(group)
        if len(group) >= 4:
            if vt([group]):
                list1.append(group)
            if len(set(group)) < 3:
                continue
            elif len(set(group)) == 3:
                list1.append(list(set(group)))

    return sorted(list1, key=lambda x: score(x), reverse=True)
        