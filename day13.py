
f = open("data13.txt")

l = []

def transpose(l):
    return [
        "".join([l[i][j] for i in range(len(l))])
        for j in range(len(l[0]))
    ]
    

def get_sym(l):
    for i in range(len(l)):
        l1,l2 = [],[]
        k1,k2 = i,i+1
        cond = True
        while k1 >=0 and k2 < len(l):
            if l[k1] != l[k2]:
                cond = False
                break
            l1.append((k1,l[k1]))
            l2.append((k2,l[k2]))
            k1 -= 1
            k2 += 1
        if cond:
            print("res",l[i::-1],l[i:])
            print("res",l1,l2)
            return i
    return -1

def get_sym3(l):
    r = []
    for i in range(len(l)):
        l1 = l[i::-1]
        l2 = l[i+1:]
        cond = True
        #print("l12",l1,l2)
        for x,y in zip(l1,l2):
            if x != y:
                cond = False
                break
        
        if cond and len(l1) != 0 and len(l2) != 0:
            #print("res",l[i::-1],l[i:])
            #print("res",l1,l2)
            #r.append(i)
            return i
    return -1

def get_sym2(l):
    for m in range(len(l)-1,-len(l),-1):
        cond = True
        if m > 0:
            i = m
            j = 0
        else:
            i = 0
            j = len(l)-m
        print(i,j)
        while i<j:
            if l[i] != l[j]:
                print(i,j,l[i],l[j])
                cond = False
                break
        if cond:
            return m
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
        print(a,b)
        #print([(i,get_sym(l,i)) for i in range(len(l))])

        l = []
    else : l.append(line)
print("S = ",S)
