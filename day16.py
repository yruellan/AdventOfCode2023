from lib import timeit, memoize

data = [list(l.strip()) for l in open("data16.txt").readlines()]

energized = [["." for _ in l] for l in data]
stack = set()

@memoize
def move(i,j,direction):
    global stack
    i += (direction==0) - (direction==2)
    j += (direction==1) - (direction==3)

    if i < 0 or j < 0:
        return
    if i >= len(data) or j >= len(data[0]):
        return
    
    energized[i][j] = "#"
    #if direction == 0: energized[i][j] = "v"
    #if direction == 1: energized[i][j] = ">"
    #if direction == 2: energized[i][j] = "^"
    #if direction == 3: energized[i][j] = "<"

    if data[i][j] == ".":
        if   direction == 0: data[i][j] = "v"
        elif direction == 1: data[i][j] = ">"
        elif direction == 2: data[i][j] = "^"
        elif direction == 3: data[i][j] = "<"
    elif data[i][j] == "/":
        if direction == 0: direction = 3
        elif direction == 1: direction = 2
        elif direction == 2: direction = 1
        elif direction == 3: direction = 0
    elif data[i][j] == "\\":
        if direction == 0: direction = 1
        elif direction == 1: direction = 0
        elif direction == 2: direction = 3
        elif direction == 3: direction = 2
    elif data[i][j] == "|":
        if direction % 2 == 1:
            stack.add((i,j,0))
            stack.add((i,j,2))
            #move(i,j,0)
            #move(i,j,2)
            return
    elif data[i][j] == "-":
        if direction % 2 == 0:
            stack.add((i,j,1))
            stack.add((i,j,3))
            #move(i,j,1)
            #move(i,j,3)
            return
    else:
        #print("not found : ",i,j,data[i][j])
        pass

    move(i,j,direction)

def make_move(i=0,j=0,d=1):
    global stack, energized

    i -= (d==0) - (d==2)
    j -= (d==1) - (d==3)
    stack.add((i,j,d))
    
    treated = set()
    itt = 0
    while len(stack) != 0:
        m = stack.pop()
        if m not in treated:
            i,j,d = m
            move(i,j,d)
            treated.add(m)
        if itt % 25 == 0 and False:
            print("itt : ",itt)
            print(stack)
            print()
        itt += 1

    S = sum(l.count("#") for l in energized)
    energized = [["." for _ in l] for l in data]
    return S

for l in data:
    #print("".join(l))
    pass
print()

for l in energized:
    #print("".join(l))
    pass

@timeit
def score():
    Smax = 0
    for i in range(len(data)):
        S1 = make_move(i,0,1)
        S2 = make_move(i,len(data[0])-1,3)
        Smax = max(S1,S2,Smax)
    for j in range(len(data[0])):
        S1 = make_move(0,j,0)
        S2 = make_move(len(data)-1,j,2)
        Smax = max(S1,S2,Smax)
    return Smax

Smax = score()
print("S = ",Smax)
