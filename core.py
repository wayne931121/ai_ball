import time, os, config
from world import World
from cycle import cycle
from object_2d import obj2d, c2d

world = World()
space_length = [9,5]

def change():
    position = c.get()
    max_ = [0,0,-1]
    i = 0
    for position_ in c.near(): #position_ is 2d index
        if position_[0]!=None and position_[1]!=None:
            index2dTo1d = spaceRoot.index(position_[0],position_[1])    
            value = space[index2dTo1d][1].result()    
            if value>max_[2]:    
                max_ = [i,index2dTo1d,value]
        i+=1    
    #jump = max(enumerate(near_index_value),key=lambda x: x[1])
    if max_[2]>7:
        c.forward(*c.near_[max_[0]])
        new_position = max_[1]
        space[new_position][0] = c.symbol
        space[position][0] = 0
        c.power -= 1
        return c.near_s[max_[0]]
    return "-"
def update():
    for i in space:
        i[1].add()    
        i[1].const = world.get()
        if i[1].result()>9: i[1].const-=9
        #if i[1].result()<0: i[1].now=-i[1].const
    position = c.get()
    v = space[position][1].result()-1
    space[position][1].decrease(v)
    c.power += v
    if c.power>c.life:
        c.power = c.life
    if c.power<0:
        c.power=0
c = c2d("●",*space_length)
c.position = [0,0]
spaceRoot = obj2d(*space_length, lambda:[0,cycle(0,2)])
space = spaceRoot.data ###
space[c.get()][0] = c.symbol
frame = cycle(0,1000)

def prettyPrint(e):
    return str(e[0])

def prettyPrint1(e):
    if e[0]==c.symbol:
        return config.n2t[str(e[1])]
    return str(e[1])

def main(root,*labels):
    if frame.now%(c.life-c.power+1)==0:
        s1 = change()
    else:
        s1 = "-"
    update()
    texts = [spaceRoot.print(prettyPrint),spaceRoot.print(prettyPrint1),s1,str(c.power),str(frame.now)]
    for t in range(len(texts)):
        labels[t].config(text=texts[t])
    frame.add()
    root.after(500,main,root,*labels)