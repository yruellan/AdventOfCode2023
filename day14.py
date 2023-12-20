
f = open("data14.txt")

data = list([list(s.strip()) for s in f.readlines()])

#for i in range(len(data[0])):
#    print("".join([data[j][i] for j in range(len(data))]))
#print()

for i in range(len(data[0])):

    j = 0
    while j < len(data):
        if j>0 and data[j][i] == "O" and data[j-1][i]==".":
            data[j][i]="."
            data[j-1][i]="O"
            j -= 1
        else:
            j += 1

    #print("".join([data[j][i] for j in range(len(data))]))

S = 0
for n,line in enumerate(data):
    for x in line:
        if x == "O":
            #print(len(data)-n)
            S += len(data)-n
print("S = ",S)
