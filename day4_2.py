
f = open("data4.txt")

cards = [1]*300

for nline,line in enumerate(f.readlines()):
    line = line.split(":")
    head = line[0]
    values = line[1]
    Id = head.split()[1]

    values = values.split("|")
    win = values[0].split()
    my_card = values[1].split()

    nb_win = 0
    for c in my_card:
        if c in win:
            nb_win += 1
            
    for i in range(nb_win):
        try:
            cards[nline+i+1] += cards[nline]
        except IndexError : print(nline,i,nline+i+1)

    #print(Id,val,win,my_card)
print(cards[:nline+1])
print("sum = ",sum(cards[:nline+1]))
