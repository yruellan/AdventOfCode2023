
f = open("data11.txt")

data = [line.strip() for line in f.readlines()]

#for line in data:
#    print(line)
#print()

void_line = []
for i,line in enumerate(data):
    if line == "."*len(line):
        void_line.append(i)

for i in reversed(void_line):
    data[i:i+1] = [data[i]]*2

data = ["".join([data[i][j] for i in range(len(data))]) for j in range(len(data[0]))]

void_col = []
for i,line in enumerate(data):
    if line == "."*len(line):
        void_line.append(i)



for i in reversed(void_line):
    data[i:i+1] = [data[i]]*2

data = ["".join([data[i][j] for i in range(len(data))]) for j in range(len(data[0]))]

#for line in data:
#    print(line)
#print()

def dist(x,y,i=None,j=None):
    if i is None and j is None:
        i,j = y
        x,y = x
    #print("dist : ",(x,y),(i,j), "=", abs(x-i) + abs(y-j))
    return abs(x-i) + abs(y-j)

stars = [(i,j) for i,l in enumerate(data) for j,x in enumerate(l) if x=="#"]
print(stars)
S = 0
for s1 in stars:
    l = [dist(s1,s2) for s2 in stars]
    s = sum(l)
    S += s
    #print(l,"  \t",s)
print("S = ",S,"->", S//2)
