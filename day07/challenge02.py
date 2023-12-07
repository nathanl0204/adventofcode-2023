dico = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

def hand_type(hand):
    card_counts = [hand.count(card) for card in hand]
    if 5 in card_counts:
        return 6
    if 4 in card_counts:
        return 5
    if 3 in card_counts:
        if 2 in card_counts:
            return 4
        return 3
    if card_counts.count(2) == 4:
        return 2
    if 2 in card_counts:
        return 1
    return 0

def replacements(hand):
    if hand == "":
        return [""]
    return [x + y for x in ("23456789TQKA" if hand[0] == "J" else hand[0]) for y in replacements(hand[1:])]

def classify(hand):
    return max(map(hand_type, replacements(hand)))

def rank(hand):
    return (classify(hand), [dico.get(card, card) for card in hand])

hands = []
fichier = open("input.txt","r")
for ligne in fichier:
    ligne.rstrip()
    hand, bid = ligne.split()
    hands.append((hand,int(bid)))
hands.sort(key=lambda hand: rank(hand[0]))
somme = 0
for strength, (hand,bid) in enumerate(hands,1):
    somme += strength * bid
print(somme)