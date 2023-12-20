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
print(location)
n = 0
while True:
    for loc in location:
        if loc[2] != "Z":break
    else : break
    
    for c in instructions:
        if c == "L": k = 0
        else : k = 1
        for i,loc in enumerate(location):
            #print(c,location,"\t",directions[location][k])
            location[i] = directions[loc][k]
        n+=1
    


print("n = ",n)
print("loc = ",location)
print("instruction = ",instructions)
print(directions)
