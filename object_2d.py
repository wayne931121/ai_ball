class obj2d:
    def __init__(self,width,height,initfun=lambda:0,*initargs):
        self.data = [initfun(*initargs) for i in range(width*height)]
        self.width = width
        self.height = height
    def index(self,column,row):
        return row*self.width+column
    def print(self,pretty=lambda x:str(x)):
        s = ""
        for r in range(self.height):
            for c in range(self.width):
                p = self.index(c,r)
                s += pretty(self.data[p])
            s+="\n"
        return s
    def get(self):
        return self.data

class c2d:
    def __init__(self,symbol,width,height):
        #                w,h
        self.position = [0,0]
        self.width = width
        self.height = height
        self.symbol = symbol
        self.near_ = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,1,0],[1,0,0,1],[0,1,1,0],[0,1,0,1]]
        self.near_s = ["←","→","↑","↓","↖","↙","↗","↘"]
        self.power = 0
        self.life = 9
    def index(self,c,r):
        return self.width*r+c
    def get(self):
        return self.index(self.position[0],self.position[1])
    def set(self,c,r):
        self.position = [c,r]
    def add(self,v,lastIndex,return_=0):
        if v==lastIndex: return return_
        return v+1
    def nadd(self,v,lastIndex,return_="last"):
        if v==0 and return_=="last": return lastIndex
        if v==0: return return_
        return v-1
    def forward_(self,left=0,right=0,up=0,down=0):#0 or 1
        if left and right:
            left = 0
            right = 0
        if up and down:
            up = 0
            down = 0
        c = self.position[0]; r = self.position[1];
        lw = self.width-1; lh = self.height-1;
        add = self.add; nadd = self.nadd;
        if left:c=nadd(c,lw,None)
        if right: c=add(c,lw,None)
        if up: r=nadd(r,lh,None)
        if down: r=add(r,lh,None)
        return [c,r]
    def forward(self,left=0,right=0,up=0,down=0):
        self.position = self.forward_(left,right,up,down)
        return self.get()
    def near(self):
        f = self.forward_
        return [f(*i) for i in self.near_]

if __name__=="__main__":
    from cycle import cycle
    a2d = obj2d(9,4,lambda x:[0,cycle(1,2,1)],3)
    a2d.data[0][1].add()
    a2d.print(lambda x:str(x[0])+str(x[1])+" ")
    b2d = obj2d(9,4,lambda:1)
    b2d.print()
    #0  1  2  3  4  5  6  7  8
    #9 10 11 12 13 14 15 16 17
    cd2d = c2d(None,9,2)
    print(cd2d.get())
    print(cd2d.forward_(0,1,1,0))