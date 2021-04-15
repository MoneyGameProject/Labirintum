import levels
from levels import levels
from playground import root, canvas, startlevel, CreateLevel, walls, doors, keys, exits, players, ups, secrets, traps, names
import time
import math
from random import*
from leaderboardprogram import leaderbordSave
# используй name=names[0] дебил!
Cl=0
stime=0
startlevel(levels[Cl])
isshifting=False
# стандареная скорость
Dspeed=6
speed=Dspeed
rup=0
brakercount=0
alreadyactive=False
def upstop():
    global Dspeed
    global speed
    global rup
    global secrets
    global players
    rup=0
    player=players[0]
    speed=Dspeed
    canvas.itemconfig(player, fill='blue', outline="blue")
    for item in secrets:
        canvas.itemconfig(item, fill='black', outline="black")
def shiftpress():
    global speed
    global Dspeed
    global players
    global isshifting
    player = players[0]
    if isshifting==True:
        isshifting=False
        speed=Dspeed
        canvas.itemconfig(player, fill='blue', outline="blue")
    else:
        isshifting=True
        speed/=2
        canvas.itemconfig(player, fill='#000069', outline="#000069")
def playermove(event):
    global names
    global alreadyactive
    global Cl
    global walls
    global doors
    global keys
    global exits
    global players
    global stime
    global speed
    global rup
    global brakercount
    global secrets
    global ups
    global traps
    key = event.keysym
    if key != "Up" and key != "Down" and key != "Left" and key != "Right" and key != 'Shift_L':
        return
    player=players[0]
    x = 0
    y = 0
    if key == 'Shift_L':
        shiftpress()
    if stime == 0:
        stime = time.time()
    if key == "Up":
        y = -speed
    if key == "Down":
        y = speed
    elif key == "Left":
        x = -speed
    elif key == "Right":
        x = speed
    canvas.move(player, x, y)
    if not player in canvas.find_overlapping(15, 15, 417, 417):
            canvas.move(player, -x, -y)
    for wall in walls:
        x1, y1, x2, y2 = canvas.coords(wall)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            if brakercount>0:
                canvas.delete(wall)
                walls.remove(wall)
                brakercount-=1
                if brakercount==0:
                    canvas.itemconfig(player, fill='blue', outline="blue")
                    rup=0
            canvas.move(player, -x, -y)
    for item in keys:
        x1, y1, x2, y2 = canvas.coords(item)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete(item)
            keys.remove(item)
            if len(keys)==0:
                for door in doors:
                    canvas.itemconfig(door, fill='green', outline="green")
# UPS HERE
    for item in ups:
        x1, y1, x2, y2 = canvas.coords(item)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            if rup==0:
                rup=randint(1,4)
                canvas.delete(item)
                ups.remove(item)
                if rup==1:
                    canvas.itemconfig(player, fill='#00ffff', outline="#00ffff")
                    speed*=2
                    root.after((10*1000),upstop)
                if rup==2:
                    canvas.itemconfig(player, fill='#0f003d', outline="#0f003d")
                    brakercount=3
                if rup==3:
                    canvas.itemconfig(player, fill='#dbdbff', outline="blue")
                    for item in secrets:
                        canvas.itemconfig(item, fill='white', outline="black")
                    root.after((3*1000),upstop)
                if rup==4:
                    for item in traps:
                        canvas.itemconfig(item, fill='red', outline="#b2ff00")
                        rup=0
# TRAP HERE
    for item in traps:
        x1, y1, x2, y2 = canvas.coords(item)
        if player in canvas.find_overlapping(x1, y1, x2, y2) and isshifting==False:
            canvas.delete(item)
            traps.remove(item)
            speed=0
            canvas.itemconfig(player, fill='#00ad86', outline="#007378")
            root.after((2*1000),upstop)
        elif player in canvas.find_overlapping(x1, y1, x2, y2) and isshifting==True:
            canvas.itemconfig(item, fill='red', outline="#b2ff00")

    for item in doors:
        x1, y1, x2, y2 = canvas.coords(item)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            if canvas.itemcget(item, 'fill')=='red':
                canvas.move(player, -x, -y)
    for exit in exits:
        x1, y1, x2, y2 = canvas.coords(exit)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete('all')
            Cl += 1
            if Cl < len(levels):
                CreateLevel(levels[Cl]) 
            else:
                canvas.unbind_all('<Key>')
                canvas.create_text(180, 160, text="You Won The Game", fill="green", font="Verdana 20 bold", anchor='center')
                ftime = round(time.time()-stime,3)
                time2 = int(ftime)
                seconds = str(time2%60)
                minutes = str(time2//60)
                print(ftime)
                sec=(math.floor(ftime))
                
                msec = str(round((ftime-sec)*1000))
                xtime=(minutes+'.'+seconds+'.'+msec)
                txt=('your time is '+ xtime)
                canvas.create_text(180, 200, text=txt, fill="green", font="Verdana 15 bold",)
                name=names[0]
                leaderbordSave(name, xtime)
                return
 

canvas.bind_all('<Key>', playermove)
 
root.mainloop()

