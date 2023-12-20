import numpy as np

f = open("data8.txt")

instructions = ""
directions = dict()

for itt,line in enumerate(f.readlines()):
    if itt==0:
        instructions = line.strip()
        #print([i for i in line.strip()])
        continue

    if line == "\n": continue

    line = line.strip().replace(" ","").split("=")
    a = line[0]
    direct = line[1].replace("(","").replace(")","")
    directions[a] = direct.split(",")
        

location = [x for x in directions.keys() if x[2]=="A"]

n = 0

def nb_step(loc):
    n = 0
    while True:
        if loc[2] == "Z":break
    
        for c in instructions:
            if c == "L": k = 0
            else : k = 1
            loc = directions[loc][k]
            n+=1
    return n

print(location)
l = [nb_step(loc) for loc in location]
print(l)
prod = 1
g = 1
print("lcm",np.lcm.reduce(l))
    

#print("loc = ",location)
print("instruction = ",instructions)
#print(directions)
