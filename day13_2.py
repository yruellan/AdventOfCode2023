
f = open("data13.txt")

l = []

def transpose(l):
    return [
        "".join([l[i][j] for i in range(len(l))])
        for j in range(len(l[0]))
    ]
    

def get_sym3(l):
    r = []
    for i in range(len(l)):
        l1 = l[i::-1]
        l2 = l[i+1:]
        cond = True
        smug = 0
        #print("l12",l1,l2)
        for x,y in zip(l1,l2):
            for a,b in zip(x,y):
                if a != b:
                    smug += 1
            if smug > 1:
                cond = False
                break
        
        if cond and len(l1) != 0 and len(l2) != 0 and smug == 1:
            #print("res",l[i::-1],l[i:])
            #print("res",l1,l2)
            #r.append(i)
            return i
    return -1


            
S = 0
for line in f.readlines():
    line = line.strip()

    if line == "":
        #i = 0            
        
        a = get_sym3(transpose(l))+1
        b = get_sym3(l)+1
        if a != 0:
            S += a
        if b != 0:
            S += 100*b
        #print(a,b)
        #print([(i,get_sym(l,i)) for i in range(len(l))])

        l = []
    else : l.append(line)
print("S = ",S)
