from collections import Counter

cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

def rank(card):
    return cards.index(card)

def hand_type(hand):
    card_counts = Counter(hand)
    if len(card_counts) == 1:
        return ("Five of a kind", 6)
    elif len(card_counts) == 2:
        if 4 in card_counts.values():
            return ("Four of a kind",5)
        else:
            return ("Full house",4)
    elif len(card_counts) == 3:
        if 3 in card_counts.values():
            return ("Three of a kind",3)
        else:
            return ("Two pair",2)
    elif len(card_counts) == 4:
        return ("One pair",1)
    else:
        return ("High card",0)

def compare_hands(hand1,hand2):
    result1 = hand_type(hand1)
    result2 = hand_type(hand2)
    if result1[0] != result2[0]:
        return result1[1] > result2[1]
    for card1, card2 in zip(hand1,hand2):
        if rank(card1) != rank(card2):
            return rank(card1) > rank(card2)
    return False

def sort_hands(hands):
    for i in range(1,len(hands)):
        key = hands[i]
        j = i - 1
        while j >= 0 and compare_hands(key,hands[j]):
            hands[j + 1] = hands[j]
            j -= 1
        hands[j + 1] = key
    return hands

hands = []
bids = []
fichier = open("input.txt","r")
L = fichier.readlines()
L = [ligne.rstrip() for ligne in L]
for ligne in L:
    values = ligne.split()
    hands.append(values[0])
    bids.append(values[1])
fichier.close()
dico = dict(zip(hands,bids))
hands = sort_hands(hands)
dico = {cle: dico[cle] for cle in hands}
bids = list(dico.values())[::-1]
somme = 0
for i in range(len(bids)):
    somme += (i+1) * int(bids[i])
print(somme)