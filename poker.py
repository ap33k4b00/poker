hand = input("Enter a hand of cards (or 'q' to quit): ").split()
straight_m = "12345678910JQKA"
high_dict = {'1': 0, '0': 1, 'J': 2, 'Q': 3, 'K': 4, 'A': 5}
straight = False
flush = False
high_straight = False
h_cards = []
l_cards = []
values = []
suites = []
ranks = [0] * 10
for i in hand:
    if len(i) == 2:
        if i[0] in high_dict.keys():
            h_cards.append(str(i[0]))
            values.append(i[0])
        else:
            l_cards.append(str(i[0]))
            values.append(i[0])
        suites.append(i[1])
    else:
        h_cards.append(str(i[0]) + str(i[1]))
        values.append(10)
        suites.append(i[2])
values_dict = {i: values.count(i) for i in values}
suites_dict = {i: suites.count(i) for i in suites}
high_cards = ''.join(sorted(''.join(h_cards), key=lambda x: high_dict[x]))
if len(h_cards) > 0 and len(l_cards) > 0:
    x = ''.join(map(str, sorted(list(map(int, l_cards))))) + high_cards
    if x in straight_m:
        straight = True
        ranks[5] = "Straight"
elif len(h_cards) > 0 and len(l_cards) == 0:
    if high_cards in straight_m:
        straight = True
        ranks[5] = "Straight"
        high_straight = True
for k, v in values_dict.items():
    if v == 1:
        ranks[9] = "High Card"
    elif v == 2 and "Three of a Kind" not in ranks:
        ranks[8] = "One Pair"
    elif v == 2 and "One Pair" in ranks:
        ranks[7] = "Two Pairs"
    elif v == 2 and "Three of a Kind" in ranks or v == 3 and "One Pair" in ranks:
        ranks[3] = "Full House"
    elif v == 3:
        ranks[6] = "Three of a Kind"
    elif v == 4:
        ranks[2] = "Four of a Kind"
for v in suites_dict.values():
    if v == 5:
        ranks[4] = "Flush"
        flush = True
    if straight and flush:
        ranks[1] = "Straight Flush"
    if high_straight and flush:
        ranks[0] = "Royal Flush"

for i in ranks:
    if i != 0:
        print(i)
        break
