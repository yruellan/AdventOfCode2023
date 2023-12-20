import collections
from recordclass import recordclass

f = open("data20.txt")

Module = recordclass('Module', ('type','value','destination'))
flipflop = "flipflop"
conjunction = "conjunction"
broadcaster = "broadcaster"

modules = dict()

for line in f.readlines():
    
    line = line.strip().split("->")[:2]
    dest = line[1].replace(" ","").split(",")
    line[0] = line[0].strip()
    if (line[0][0] == "%"):
        m = Module(flipflop,0,dest)
        name = line[0][1:]
    elif (line[0][0] == "&"):
        m = Module(conjunction,dict(),dest)
        name = line[0][1:]
    elif (line[0] == broadcaster):
        m = Module(broadcaster,0,dest)
        name = broadcaster
    else :
        raise Exception(f"Bad type for {line = }")
    #print(name,m)
    modules[name] = m

for name,m in modules.items():
    for dest in m.destination:
        if dest in modules.keys() and modules[dest].type == conjunction:
            modules[dest].value[name] = 0

low = 0
high = 0
def push(i):
    global low,high

    #print("button","-low ->",broadcaster)
    stack = [(broadcaster,0,"button")]

    while len(stack) > 0:

        name,val, owner = stack.pop(0)
        if name =="rx" and val == 0:
            print("objective :",i)
        if val == 0:
            low += 1
            #print(owner,"-low ->",name)
        else :
            high += 1
            #print(owner,"-high ->",name)
        if name not in modules.keys():
            continue
        m = modules[name]
        
        if m.type == flipflop:
            
            if val==True or val==1:
                continue
            else:
                m.value = 1 - m.value
                for dest in m.destination:
                    
                    stack.append((dest,m.value,name))
                continue

        elif m.type == conjunction:

            if owner is None:
                raise Exception(f"Conjunction need a predecessor")

            m.value[owner] = val
            if False in m.value.values():
                for dest in m.destination:
                    stack.append((dest,1,name))
                continue
            else :
                for dest in m.destination:
                    stack.append((dest,0,name))
                continue
            

        elif m.type == broadcaster:
            for dest in m.destination:
                stack.append((dest,val,name))
            continue
        
    

print()
for i in range(1000):
    push(i)
    if i%100 == 0 or i == 999:
        print(f"res = ({i:4}) : {low:6},{high:6},{low*high:15}")



