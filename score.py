def score(cards):
    '''take a list of cards as an argument, return the combined score
    of the cards'''
    dic = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13, 'X': 1000}
    count = 0
    for card in cards:
        count += dic[card[0]]
    return count