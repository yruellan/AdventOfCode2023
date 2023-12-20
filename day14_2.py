from time import time
from functools import cache
from tqdm import tqdm

f = open("data14.txt")

#for i in range(len(data[0])):
#    print("".join([data[j][i] for j in range(len(data))]))
#print()

@cache
def roll_north(data):
    data = list([list(s) for s in data])
    for i in range(len(data[0])):

        j = 0
        while j < len(data):
            if j>0 and data[j][i] == "O" and data[j-1][i]==".":
                data[j][i]="."
                data[j-1][i]="O"
                j -= 1
            else:
                j += 1
    return tuple(["".join(s) for s in data])

@cache
def roll_south(data):
    data = list([list(s) for s in data])
    for i in range(len(data[0])):

        j = len(data)-1
        while j >= 0:
            if j<len(data)-1 and data[j][i] == "O" and data[j+1][i]==".":
                data[j][i]="."
                data[j+1][i]="O"
                j += 1
            else:
                j -= 1
    return tuple(["".join(s) for s in data])

@cache
def roll_west(data):
    data = list([list(s) for s in data])
    for i in range(len(data)):

        j = 0
        while j < len(data[0]):
            if j>0 and data[i][j] == "O" and data[i][j-1]==".":
                data[i][j]="."
                data[i][j-1]="O"
                j -= 1
            else:
                j += 1
    return tuple(["".join(s) for s in data])

@cache
def roll_east(data):
    data = list([list(s) for s in data])
    for i in range(len(data)):

        j = len(data[0])-1
        while j >= 0:
            if j<len(data[0])-1 and data[i][j] == "O" and data[i][j+1]==".":
                data[i][j]="."
                data[i][j+1]="O"
                j += 1
            else:
                j -= 1
    return tuple(["".join(s) for s in data])

@cache
def roll(data):
    data = roll_north(data)
    data = roll_west(data)
    data = roll_south(data)
    data = roll_east(data)
    return data

@cache
def roll1000(data):
    for _ in range(1000):
        data = roll(data)
    return data

def load_val(data):
    S = 0
    for n,line in enumerate(data):
        for x in line:
            if x == "O":
                #print(len(data)-n)
                S += len(data)-n
    return S

def print_data(data):
    for line in data:
        print("".join(line))
    print()

data = tuple([s.strip() for s in f.readlines()])
t0 = time()
#l = []
n = 1000000
for i in (range(n)):
    #print(type(data))
    data = roll1000(data)

    #for line in data:
    #    print("".join(line))
    #print()
    
    #l.append( load_val(data) )
    #if i%1 == 0 : print(f"S ({i:4}) = {l[-1]}")
    #b = True
    #if i>100 and False:
    #    print("break",i)
    #    break
    if (i*100)%n == 0 :
        print(f"itt : {(i*100)//n:5}, {time()-t0:.3f}")
    
t1 = time()

print("S = ",load_val(data))
print("dt = ", f"{t1-t0:.3f}")
