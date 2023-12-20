f = open("data6.txt")



data = f.readlines()

Time = data[0].split(":")[1].split()
Dist = data[1].split(":")[1].split()
Wins = [0]*len(Time)

#print(Time,Dist)

for i,(t,d) in enumerate(zip(Time,Dist)):
    t = int(t)
    d = int(d)

    prev = 0
    for tc in range(1,d):
        dc = tc*(t-tc)
        #print("\tcharge",tc,"->", dc)
        if dc > d : Wins[i] += 1
        elif dc < prev: break
        prev = dc
    print()

print(Wins)
p = 1
for w in Wins : p*=w
print("p :", p)
