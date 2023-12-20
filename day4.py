
f = open("data4.txt")

S = 0

for line in f.readlines():
    line = line.split(":")
    head = line[0]
    cards = line[1]
    Id = head.split()[1]

    cards = cards.split("|")
    win = cards[0].split()
    my_card = cards[1].split()

    val = 0
    for c in my_card:
        if c in win:
            if val == 0: val=1
            else : val *= 2
    S += val

    #print(Id,val,win,my_card)
print("sum = ",S)
