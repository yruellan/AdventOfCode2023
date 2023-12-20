
f = open("data19.txt")


workflow = dict()
parts = []
is_part1 = True
wf_val = dict()

for line in f.readlines():
    if line == "\n":
        is_part1 = False
        continue
    if is_part1:
        name,value = line.strip().replace("}","").split("{")
        value2 = []
        for v in value.split(","):
            x = v.split(":")
            if len(x) == 1:
                value2.append(x[0])
                break
            cond,part = x[:2]
            value2.append( (cond[0],cond[1],int(cond[2:]),part) )

        #print(name,value2)
        workflow[name] = value2
    else:
        obj = dict()
        for x in line.strip().replace("{","").replace("}","").split(","):
            key,val = x.split("=")[:2]
            obj[key] = int(val)
        parts.append(obj)
        #print(obj)

    for key in workflow.keys():
        wf_val[key] = []


def add_to_wf(obj,wf):
    #print("wf : ",wf)
    for cond in workflow[wf]:
        if cond == "A":
            wf_val[wf].append(obj)
            #print("append : ",wf)
            return True
        elif cond == "R":
            #print("reject : ",wf)
            return False
        elif type(cond) is str:
            #print("rec : ",cond)
            return add_to_wf(obj,cond)
            #if add_to_wf(obj,cond): return True
            #else : continue

        
        if cond[1]==">":comp = lambda x,y : x>y
        else : comp = lambda x,y : x<y
        
        if comp(obj[cond[0]],cond[2]):
            #print("verify cond : ",wf,cond)
            if cond[3] == "A":
                #print("append2 : ",wf)
                wf_val[wf].append(obj)
                return True
            elif cond[3] == "R":
                #print("reject2 : ",wf)
                return False
            else:
                #print("rec2",cond)
                return add_to_wf(obj,cond[3])
                #if add_to_wf(obj,cond[3]): return True
        else :
            #print("reject cond: ",wf,cond)
            pass

def asignation():
    
    for obj in parts:
        #print(obj)
        add_to_wf(obj,"in")
        #print()
                    
    #print(wf_val)

def get_score():
    score = 0
    for val in wf_val.values():
        for obj in val:
            sc_obj = obj["x"]+obj["m"]+obj["a"]+obj["s"]
            print(obj,sc_obj)
            score += sc_obj
    print("score = ",score)

asignation()
get_score()





