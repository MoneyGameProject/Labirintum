from tkinter import*
import levels
root=Tk()
root.geometry('400x400')
side=24
canvas = Canvas (root, height=(side*18), width=(side*18), relief=SOLID, bg='white')
walls=[]
doors=[]
keys=[]
exits=[]
players=[]
secrets=[]
ups=[]
traps=[]
names=[]
lvl=''
def entername():
    global lvl
    global names
    global E1
    global L1
    global B1
    n=E1.get()
    names.append(str(n))
    if names[0]!='':
        L1.forget()
        E1.forget()
        B1.forget()
        canvas.pack(expand=True)
        CreateLevel(lvl)
    else:
        names[0]='unknown'
        L1.forget()
        E1.forget()
        B1.forget()
        canvas.pack(expand=True)
        CreateLevel(lvl)

def startlevel(arg):
    global lvl
    global L1
    global B1
    global lvl
    global E1
    lvl = arg
    L1=Label(root, text='Enter name:')
    E1=Entry(root, )
    B1=Button(root, text='Enter', command=entername,)
    L1.pack()
    E1.pack()
    B1.pack()
def CreateLevel(level):
    global names
    global walls
    global doors
    global keys
    global exits
    global players
    global secrets
    global ups
    global traps
    global side
    ups.clear()
    walls.clear()
    doors.clear()
    keys.clear()
    exits.clear()
    players.clear()
    secrets.clear()
    traps.clear()
    x=0
    y=0
    for line in level:
        x=0
        for block in line:
            if block=='W':
                Wall = canvas.create_rectangle(x, y, x+side, y+side, fill='black', outline='black',)
                walls.append(Wall)
            if block=='K':
                Key = canvas.create_rectangle(x, y, x+side, y+side, fill='yellow', outline='yellow',)
                keys.append(Key)
            if block=='D':
                Door = canvas.create_rectangle(x, y, x+side, y+side, fill='red', outline='red',)
                doors.append(Door)
            if block=='E':
                Exit = canvas.create_rectangle(x, y, x+side, y+side, fill='orange', outline='orange',)
                exits.append(Exit)
            if block=='P':
                Player = canvas.create_rectangle(x+1, y+1, x+side-1, y+side-1, fill='blue', outline='blue',)
                players.append(Player)
            if block=='S':
                Secret = canvas.create_rectangle(x, y, x+side, y+side, fill='black', outline='black',)
                secrets.append(Secret)
            if block=='U':
                Up = canvas.create_rectangle(x+5, y+5, x+side-5, y+side-5, fill='purple', outline='purple',)
                ups.append(Up)
            if block=='T':
                Trap = canvas.create_rectangle(x+5, y+5, x+side-5, y+side-5, fill='white', outline='white',)
                traps.append(Trap)
            x+=side
        y+=side

'''if __name__=="__main__":
    CreateLevel(levels.level1)'''
