

def h(s=0):
    if s == "0": return 0
    x = 0
    for c in s:
        x += ord(c)
        x *= 17
        x  %= 256
    return x

line = open("data15.txt").readlines()[0]
line = line.strip().split(",")

Box = [[]]*256

for x in line:
    #print(x)
    if x.count("-"):
        loc = x.split("-")[0]
        i = h(loc)

        Box[i] = [
            (a,b)
            for (a,b) in Box[i]
            if a != loc
        ]

    if x.count("="):
        loc,n = x.split("=")[:2]
        i = h(loc)
        Box[i] = [
            (a,b)
            if a != loc
            else (loc,int(n))
            for (a,b) in Box[i]
        ]
        if (loc,int(n)) not in Box[i]:
            Box[i].append( (loc,int(n)) )

    #print(Box)

S = 0
for i,l in enumerate(Box):
    for j,(a,b) in enumerate(l):
        S += (i+1) * (j+1) * b
print("S =",S)
