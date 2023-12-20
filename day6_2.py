import tqdm

f = open("data6.txt")


data = f.readlines()

Time = int(data[0].split(":")[1].replace(" ",""))
Dist = int(data[1].split(":")[1].replace(" ",""))
Wins = 0

print(Time,Dist)


prev = 0
for tc in range(1,Dist):
    dc = tc*(Time-tc)
    #print("\tcharge",tc,"->", dc)
    if dc > Dist : Wins += 1
    elif dc < prev: break
prev = dc
print()

print(Wins)
print("p :", 0)

# SupSyDeMarciou
