import tkinter as tk
import time

class Tower():
    
    def __init__(self,x,y,SIZE=0):
        self._stack=[]
        for i in range(SIZE,0,-1):
            self._stack.append(i)
        self.size = SIZE
        self.x = x
        self.y = y

    def push(self,el):
        self._stack.append(el)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self._stack.pop()


root = tk.Tk()
root.geometry('1000x700+0+0')
root.title("Tower Of Hanoi")

Towers = []
all_rect=[]
ytop=100
disty = 5
distx = 5
S_no = 1
allow_interaction = False
colors = ['blue','green','red','#123456','yellow','orange']
background = tk_rgb = "#%02x%02x%02x" % (100, 40, 54)

sleep = 0
size=300
DEC_IN_WIDTH=20
w=20

can = tk.Canvas (root,width=1000,height=800,bg=background)
can.grid()

def init(START,FINISH,DISKS=4,SLEEP=10):
    global sleep
    global ytop
    global allow_interaction
    
    sleep = SLEEP
    start = START if 0<START<4 else 1
    finish = FINISH
    
    disks = DISKS if DISKS else 4
    if disks>15:
        disks = 4
        print('Too many disks')
        print('Now using only %s disks'%4)
    ytop += disks*w + 30

    if disks > 6:
        import random
        for itr in range(disks-6):
            color = '#'+str(random.randint(120000,999999))
            colors.append(color)

    in_disk = {1:0,2:0,3:0}         ## initial disks given 
    in_disk[start] = disks
    Tower1 = Tower(200,600,in_disk[1])
    Tower2 = Tower(500,600,in_disk[2])
    Tower3 = Tower(800,600,in_disk[3])

    stand(Tower1,Tower2,Tower3)
    rect(Tower1)
    rect(Tower2)
    rect(Tower3)
    Towers.extend([0,Tower1,Tower2,Tower3])

    ##allow_interaction = True
    TOH(disks,start,finish,6 - start - finish)
    
def stand(*args):
    size = 0
    for tower in args:
        size = max(tower.size,size)
    for tower in args:
        x, y = tower.x, tower.y 
        rect = can.create_rectangle(x-5,y+w*2,x+5,y-w*size-w*4,fill='grey',width=3)

def rect(tower):
    x=tower.x
    y=tower.y
    
    for i in range(tower.size):
        p =(size - DEC_IN_WIDTH*i)//2
        rect = can.create_rectangle(x-p,y-w*i,x+p,y+w-w*i,fill=colors[i],width=3)
        all_rect.insert(0,rect)
    root.update()



def move(tow1,tow2):
    size = Towers[tow1].size
    box_number = Towers[tow1].pop()
       
    uptimes = (ytop + (6-size)*w)//disty
    for rep in range(uptimes):
        can.move(all_rect[box_number-1],0,-disty)
        root.update()
        root.after(sleep)

    mul = 1 if tow2>tow1 else -1
    hori_times = abs(300*(tow2-tow1))//distx
    for rep in range(hori_times):
        can.move(all_rect[box_number-1],mul*distx,0)
        root.update()
        root.after(sleep)

    size = Towers[tow2].size

    downtimes = (ytop + (5-size)*w)//disty
    for rep in range(downtimes):
        can.move(all_rect[box_number-1],0,+disty)
        root.update()
        root.after(sleep)

    Towers[tow2].push(box_number)

def TOH(disks,tower1,tower2,tower3):
    global S_no
    if disks == 1:
        if allow_interaction:
            print(S_no,'Move top disk from %d to %s'%(tower1,tower2))
        S_no += 1
        move(tower1,tower2)
        return
    TOH(disks-1,tower1,tower3,tower2)
    if allow_interaction:
        print(S_no,'Move top disk from %d to %s'%(tower1,tower2))
    S_no += 1
    move(tower1,tower2) 
    TOH(disks-1,tower3,tower2,tower1)
    
init(2,3,15,-1)  ## start tower, finish tower, disks, sleep

time.sleep(2)
