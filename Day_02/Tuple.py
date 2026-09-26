cards = ("heart", "spade", "diamond", "club")

for card in cards:
    print(card.upper())

l_cards = list(cards)
l_cards.append("random")
cards = list(cards)
print(cards)

t1 = (1,2,3)
t2 = (10,20,30)
t3 = ("one", "two")

t1,t2 = t2,t1
print(t1)
print(t2)

n1,n2,n3 = t1
print(n2)


zipped = tuple(zip(t1,t2,t3))
print(zipped)

for a,b,c in zipped:
    print(f"{a}, {b}, {c}")