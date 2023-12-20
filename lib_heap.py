

class heap:

    def __init__(self):
        self.size = 1
        self.nb = 0
        self.data = [None]

    def __len__(self):
        return self.nb

    #@profile
    def add(self,e,prio):
        if self.nb == self.size:
            self.data += [None]*self.size
            self.size *= 2

        self.data[self.nb] = (e,prio)
        self.nb += 1
        i = self.nb-1
        while i!=0:
            j = i//2
            if self.data[i][1] > self.data[j][1]:
                self.data[i],self.data[j] = self.data[j],self.data[i]
                i = i//2
            else : break

    #@profile
    def pop(self):

        if self.nb == 0:
            raise IndexError
        
        e = self.data[0][0]
        self.nb -= 1
        self.data[0] = self.data[self.nb]
        self.data[self.nb] = None
        
        i = 0
        while True:
            
            j = 2*i+1
            if j >= self.nb : break
            
            if j+1 < self.nb and self.data[j][1] < self.data[j+1][1]: j+= 1
                
            if self.data[i][1] < self.data[j][1]:
                self.data[i],self.data[j] = self.data[j],self.data[i]
                i = j
            else : break

        return e

    def __repr__(self):
        d = dict()
        for (e,p) in self.data[:self.nb]:
            d[e]=p
        return d.__repr__()

if __name__ == "__main__":
    h = heap()
    h.add(1,10)
    h.add(3,30)
    h.add(2,20)
    print(h,h.data)
    print(h.pop())
    print(h,h.data)
    print(h.pop())
    print(h,h.data)
    print(h.pop())
    print(h,h.data)
