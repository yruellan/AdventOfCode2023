

#f = open("data1.txt","r")

#s = 0
#for line in f.readlines():
#    b = ""
#    for char in line:
#        if char in "1234567890":
#            b += char
#    n = b[0]+b[-1]
#    n = int(n)
#    s += n
#print(s)

f = open("data1bis.txt","r")
s = 0
num=0
for line in f.readlines():
    b=""
    for i,c in enumerate(line):
        if c in "1234567890":
            b+=c
        if line[i:].startswith("one"):b+="1"
        if line[i:].startswith("two"):b+="2"
        if line[i:].startswith("three"):b+="3"
        if line[i:].startswith("four"):b+="4"
        if line[i:].startswith("five"):b+="5"
        if line[i:].startswith("six"):b+="6"
        if line[i:].startswith("seven"):b+="7"
        if line[i:].startswith("eight"):b+="8"
        if line[i:].startswith("nine"):b+="9"
        if line[i:].startswith("zero"):b+="0"
    if num < 5: print(b)
    n = b[0]+b[-1]
    s += int(n)
    num += 1
print("s=",s)
