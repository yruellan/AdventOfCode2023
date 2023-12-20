

def prediction(l):
    #print(l)
    if l == [0]*len(l):
        return 0

    l2 = [l[i+1] - l[i] for i in range(len(l)-1)]
    return l[0]-prediction(l2)


f = open("data9.txt")

S = 0
for line in f.readlines():

    #print(line)
    line = line.strip().split(" ")
    val = prediction([int(x) for x in line])
    print("val = ",val)
    S += val
print("S = ",S)
