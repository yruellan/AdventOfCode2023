
f = open("data10.txt")

data = [l.strip() for l in f.readlines()]

dist = 0
a,b = 0,0
prev = None
#print("data",data)

for i,line in enumerate(data):
    if "S" in line:
        a = i
        b = line.index("S")
        break

def voisin(a,b):
    l = []
    if a>0 and data[a-1][b] in "S|7F": l.append((a-1,b))
    if b>0 and data[a][b-1] in "S-LF": l.append((a,b-1))
    if a<len(data)-1 and data[a+1][b] in "S|LJ": l.append((a+1,b))
    if b<len(data)-1 and data[a][b+1] in "S-J7": l.append((a,b+1))
    #print("voisin",a,b,"=",l,"\t",a>0,b>0,a<len(data)-1,b<len(data)-1)
    return l

while True:

    if dist > 0 and data[a][b] == "S": break
    
    #print(a,b,"\t",dist,"\t")
    for v in voisin(a,b):
        
        if v != prev and (a,b) in voisin(v[0],v[1]):
            #print("next",(a,b),"->",v,"\t",prev,"  \t",dist)
            prev = a,b
            a,b = v
            dist += 1
            break

    
    
    
    
print("end",a,b,"\t",prev,dist)
print("dist max",dist//2)
