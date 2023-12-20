
f = open("data7.txt")

cards = []
points = []
bid = []
data = []

def get_value(card):

    hand = dict()
    for c in card:
        try:
            hand[c] += 1
        except KeyError:
            hand[c] = 1

    if 'J' in card and card != "JJJJJ":
        card2 = [get_value(card.replace('J',c)) for c in hand if c != "J"]
        s = max(card2)
        for i,c in enumerate(card):
            if c == "J":
                s[i+1] = -1
        return s
    
    if 5 in hand.values():
        points = 7
    elif 4 in hand.values():
        points = 6
    elif 3 in hand.values() and 2 in hand.values():
        points = 5
    elif 3 in hand.values():
        points = 4
    elif list(hand.values()).count(2) == 2:
        points = 3
    elif 2 in hand.values():
        points = 2
    else:
        points = 1
        
    values = [points]
    for c in card:
        if c == 'A': values.append(15)
        elif c == 'K': values.append(14)
        elif c == 'Q': values.append(13)
        elif c == 'T': values.append(11)
        elif c == 'J': values.append(-1)
        else : values.append(int(c))

    return values

for line in f.readlines():
    line = line.strip().split()
    card = line[0]
    
    values = get_value(card)

    data.append((card,int(line[1]),values))

for d in data:
    #print(d)
    pass

def comp(a,b):
    if a[2] > b[2] : return True
    if a[2] < b[2] : return False
    for c1,c2 in zip(a[3],b[3]):
        if c1 > c2 : return True
        if c1 < c2 : return False
    return True

#print()
s = 0
data.sort(key=lambda x: x[2])
for i,d in enumerate(data):
    #print(d)
    s += (1+i) * d[1]
print("\ns = ",s)
