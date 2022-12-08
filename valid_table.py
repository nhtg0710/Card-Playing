def valid_table(groups):
    '''take a list of lists of cards, return a boolean to check
    if the state of the table is valid or not'''
    dic1 = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}
    dic2 = {'S': 'b', 'C': 'b', 'D': 'r', 'H': 'r'}          
    if not groups:
        return True
    for group in groups:
        if len(group) < 3:
            return False
        if 'XX' in group:
            group.remove('XX')
        list0 = [(dic1[card[0]], card[1]) for card in group]       
        
        # sort the cards to make validating a run easier
        group = sorted(list0)         
        set0 = set()  # what suit the cards are, no repetition
        set1 = set()  # what number the cards are, no repetition
        lst0 = [group[i][1] for i in range(len(group))]  # list of suits
        lst1 = [group[i][0] for i in range(len(group))]  # list of card numbers        
        for i in range(len(group)):
            set1.add(group[i][0])
            set0.add(group[i][1])  
            
        # we want to validate an N-of-a-kind
        if len(set1) == 1:
            if ((len(group) == 3 and len(set0) < 3) or
                (len(group) >=4 and len(set0) < 4)):
                return False
       
        # we want to validate a run
        else:
            if lst1 != list(range(min(lst1), max(lst1) + 1)):
                return False
            else:
                for i in range(len(lst0) - 1):
                    if dic2[lst0[i]] == dic2[lst0[i + 1]]:
                        return False
    return True   