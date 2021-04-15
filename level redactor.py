from tkinter import*
root=Tk()
root.geometry('400x450')
canvas = Canvas (root, height=360, width=360, relief=SOLID, bg='white')
canvas.pack(expand=True)
squares=[]
mode='wall'
def space():
    global squares
    side=20
    x=0
    y=0
    for line in range(18):
        x=0
        for block in range(18):
            sqare = canvas.create_rectangle(x, y, x+side, y+side, fill='white', outline='black',)
            squares.append(sqare)
            x+=side
        y+=side

def paint(event):
    global squares
    for item in squares:
        if item in canvas.find_overlapping(event.x, event.y, event.x, event.y,):
            if mode=='wall':
                canvas.itemconfig(item, fill='black', outline="white")
            if mode=='player':
                canvas.itemconfig(item, fill='blue', outline="white")
            if mode=='key':
                canvas.itemconfig(item, fill='yellow', outline="black")
            if mode=='door':
                canvas.itemconfig(item, fill='red', outline="black")
            if mode=='up':
                canvas.itemconfig(item, fill='purple', outline="white")
            if mode=='trap':
                canvas.itemconfig(item, fill='green', outline="white")
            if mode=='exit':
                canvas.itemconfig(item, fill='orange', outline="black")
            if mode=='tunnel':
                canvas.itemconfig(item, fill='gray', outline="black")
            
def errase(event):
    global squares
    for item in squares:
        if item in canvas.find_overlapping(event.x, event.y, event.x, event.y,):
            canvas.itemconfig(item, fill='white', outline="black")
def key():
    global mode
    mode='key'
def door():
    global mode
    mode='door'
def up():
    global mode
    mode='up'
def trap():
    global mode
    mode='trap'
def Exit():
    global mode
    mode='exit'
def tunnel():
    global mode
    mode='tunnel'
def wall():
    global mode
    mode='wall'

def player():
    global mode
    mode='player'

def read():
    print(1)
    global squares
    level=[]
    line=''
    for item in squares:
        if canvas.itemcget(item, 'fill')=='white':
            line+=' '
        if canvas.itemcget(item, 'fill')=='black':
            line+='W'
        if canvas.itemcget(item, 'fill')=='yellow':
            line+='K'
        if canvas.itemcget(item, 'fill')=='red':
            line+='D'
        if canvas.itemcget(item, 'fill')=='orange':
            line+='E'
        if canvas.itemcget(item, 'fill')=='blue':
            line+='P'
        if canvas.itemcget(item, 'fill')=='gray':
            line+='S'
        if canvas.itemcget(item, 'fill')=='green':
            line+='T'
        if canvas.itemcget(item, 'fill')=='purple':
            line+='U'
        if len(line)==18:
            print(line)
            level.append(line)
            line=''
    print(level)

buttons = Frame(root,)
keyB = Button(buttons, bg='yellow', text='key', command=key)
doorB = Button(buttons, bg='red', text='door', command=door)
upB = Button(buttons, bg='purple', text='up', command=up)
trapB = Button(buttons, bg='green', text='trap', command=trap)
exitB = Button(buttons, bg='orange', text='exit', command=Exit)
tunnelB = Button(buttons, bg='grey', text='tunnel', command=tunnel)
wallB = Button(buttons, bg='black', fg='white', text='wall', command=wall)
playerB = Button(buttons, bg='blue', text='player', command=player)
reliseB = Button(root, bg='white', text='relise', command=read)
buttons.pack()
keyB.pack(side='right')
doorB.pack(side='right')
upB.pack(side='right')
trapB.pack(side='right')
exitB.pack(side='right')
tunnelB.pack(side='right')
wallB.pack(side='right')
playerB.pack(side='right')
canvas.bind('<B1-Motion>',paint)
canvas.bind('<B3-Motion>',errase)
reliseB.pack()
space()
root.mainloop()
