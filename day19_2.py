from math import log

f = open("data19.txt")


workflow = dict()
is_part1 = True
accepted = []

for line in f.readlines():
    if line == "\n":
        break
    
    
    name,value = line.strip().replace("}","").split("{")
    value2 = []
    for v in value.split(","):
        x = v.split(":")
        if len(x) == 1:
            value2.append(x[0])
            break
        cond,part = x[:2]
        value2.append( (cond[0],cond[1],int(cond[2:]),part) )

    workflow[name] = value2


def add_to_wf(obj,wf):
    #print("wf : ",wf)
    for cond in workflow[wf]:
        if cond == "A":
            accepted.append(obj)
            #print("append : ",wf)
            return True
        elif cond == "R":
            #print("reject : ",wf)
            return False
        elif type(cond) is str:
            #print("rec : ",cond)
            return add_to_wf(obj,cond)


        obj2 = {key:value[:] for key,value in obj.items()}
        if cond[1]==">":
            obj2[cond[0]][0] = cond[2]+1
            obj[cond[0]][1] = cond[2]
        else : # "<"
            obj2[cond[0]][1] = cond[2]-1
            obj[cond[0]][0] = cond[2]
        
        if True:
            if cond[3] == "A":
                #print("append2 : ",wf)
                accepted.append(obj2)
            elif cond[3] == "R":
                #print("reject2 : ",wf)
                pass
            else:
                add_to_wf(obj2,cond[3])

def asignation():

    obj = dict()
    Min = 1
    Max = 4000
    obj["x"] = [Min,Max]
    obj["m"] = [Min,Max]
    obj["a"] = [Min,Max]
    obj["s"] = [Min,Max]
    add_to_wf(obj,"in")

def get_score():
    score = 0
    for obj in accepted:
        sc_obj = 1
        for x in obj.values():
            if x[1] > x[0]:
                sc_obj *= 1 + x[1] - x[0]
        #print(f"{str(obj):75} {sc_obj}")
        score += sc_obj
    print("score = ",score)
    print("expect  ",167409079868000)
    print("delta : ",score - 167409079868000)
    #print(f"\t\t = {log(abs(score - 167409079868000),10):.3f}")
    print(score == 167409079868000)

asignation()
get_score()





