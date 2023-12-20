

def h(s=0):
    if s == "0": return 0
    x = 0
    for c in s:
        x += ord(c)
        x *= 17
        x  %= 256
    return x

for line in open("data15.txt").readlines():
    line = line.strip().split(",")
    l = [h(s) for s in line]
    print(sum(l))
