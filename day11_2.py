
f = open("data11.txt")

data = [line.strip() for line in f.readlines()]
data2= data[:]

M = 1000000

#for line in data:
#    print(line)
#print()

void_line = []
for i,line in enumerate(data):
    if line == "."*len(line):
        void_line.append(i)

#for i in reversed(void_line):
#    data2[i:i+1] = [data2[i]]*M

data_r = ["".join([data[i][j] for i in range(len(data))]) for j in range(len(data[0]))]
#data2 = ["".join([data2[i][j] for i in range(len(data2))]) for j in range(len(data2[0]))]

void_col = []
for i,col in enumerate(data_r):
    if col == "."*len(col):
        void_col.append(i)


#for i in reversed(void_col):
#    data2[i:i+1] = [data2[i]]*M

data2 = ["".join([data2[i][j] for i in range(len(data2))]) for j in range(len(data2[0]))]

if False:
    for line in data2:
        print(line)
    print()


def dist(x,y,i=None,j=None,m=0,c=False):
    if i is None and j is None:
        i,j = y
        x,y = x
    dx = [d for d in void_line if (x < d and d < i) or (i<d and d<x)]
    dy = [d for d in void_col  if (y < d and d < j) or (j<d and d<y)]
    #print("dist : ",(x,y),(i,j), "=", abs(x-i) + abs(y-j))
    if c:
        return abs(x-i) + abs(y-j),abs(x-i) + abs(y-j) + (len(dx) + len(dy)) * (m-1),dx,dy
    return abs(x-i) + abs(y-j) + (len(dx) + len(dy)) * (m-1)

stars = [(i,j) for i,l in enumerate(data) for j,x in enumerate(l) if x=="#"]
#stars2 = [(i,j) for i,l in enumerate(data2) for j,x in enumerate(l) if x=="#"]
#print(stars)
S = 0
S2 = 0
#for a,b in [(4,8),(0,6),(2,5),(7,8)]:
#for a,b in [(0,1),(0,2),(0,3)]:
#    print("dist : ",a,b, "=", dist(stars[a],stars[b],m=M,c=True),dist(stars2[a],stars2[b],m=0))
for s1 in stars:
    l = [dist(s1,s2,m=M) for s2 in stars]
    s = sum(l)
    S += s
    #print(l,"  \t",s)
#for s1 in stars2:
#    l = [dist(s1,s2,m=0) for s2 in stars2]
#    s = sum(l)
#    S2 += s
print("S = ",S,"->", S//2)
#print("S = ",S2,"->", S2//2)
