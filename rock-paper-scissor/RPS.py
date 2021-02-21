import turtle
import random
import time
from turtle import Screen
turtle.bgcolor("black")


    
scrn = turtle.Screen()
screen=Screen()

scrn.setup(2000,1080,startx=0,starty=0)


a=turtle.Turtle()
a.penup()
a.goto(-350,350)
a.pendown()
a.color("yellow")
a.write("ROCK - PAPER - SCISSOR",font=("Evil Empire",50,"normal"))

a1=turtle.Turtle()
a1.penup()
a1.goto(-250,200)
a1.pendown()
a1.color("yellow")
a1.write(" GOOD TO HAVE YOU LAD  ",font=("Algerian",20,"normal"))
time.sleep(2)

a2=turtle.Turtle()
a2.penup()
a2.goto(-370,150)
a2.pendown()
a2.color("yellow")
a2.write(" HOPE YOU ARE FEMILIAR WITH THIS GAME",font=("Algerian",20,"normal"))
time.sleep(2)

a3=turtle.Turtle()
a3.penup()
a3.goto(-450,100)
a3.pendown()
a3.color("yellow")
a3.write("GOOD NOW GET READY TO PLAY THE GAME WITH ME $$$$$$$$$",font=("Algerian",20,"normal"))
time.sleep(3)

a1.undo()
a2.undo()
a3.undo()

cntp = 0;
cntc = 0;
flag = 0;

p=turtle.Turtle()
p1=turtle.Turtle()
p2=turtle.Turtle()
c=turtle.Turtle()
c1=turtle.Turtle()
c2=turtle.Turtle()



def comp1():
    c1.shape("blank")
    c2.shape("blank")
    scrn.addshape("rockc.png")
    c.penup()
    c.goto(300,150)
    c.pendown()
    c.shape("rockc.png")
    

def comp2():
    c.shape("blank")
    c2.shape("blank")
    scrn.addshape("paperc.png")
    c1.penup()
    c1.goto(300,150)
    c1.pendown()
    c1.shape("paperc.png")
    

def comp3():
    c1.shape("blank")
    c.shape("blank")
    scrn.addshape("scissorc.png")
    c2.penup()
    c2.goto(300,150)
    c2.pendown()
    c2.shape("scissorc.png")
    

def rock():
    computer = random.choice([1,2,3])
    p1.shape("blank")
    p2.shape("blank")
    scrn.addshape("rock.png")
    p.penup()
    p.goto(-300,150)
    p.pendown()
    p.shape("rock.png")
    if(computer==1):
        flag = 0
        comp1()
        update(flag)
        print("tie")
        print(flag)
        
    
    if(computer==2):
        flag = 1
        comp2()
        update(flag)
        print("computer win")
        print(flag)
        
         
    if(computer==3):
        flag = 2
        comp3()
        update(flag)
        print("you win")
        print(flag)
        
  



def paper():
    computer = random.choice([1,2,3])
    p.shape("blank")
    p2.shape("blank")
    scrn.addshape("paper.png")
    p1.penup()
    p1.goto(-300,150)
    p1.pendown()
    p1.shape("paper.png")
    if(computer==1):
        flag = 2
        comp1()
        update(flag)
        print("you win")
        print(flag)
        
        
    if(computer==2):
        flag = 0
        comp2()
        update(flag)
        print("tie")
        print(flag)
        
    
    if(computer==3):
        flag = 1
        comp3()
        update(flag)
        print("computer win")
        print(flag)
        
    
    

def scissor():
    computer = random.choice([1,2,3])
    p.shape("blank")
    p1.shape("blank")
    scrn.addshape("scissor.png")
    p2.penup()
    p2.goto(-300,150)
    p2.pendown()
    p2.shape("scissor.png")
    if(computer==1):
        flag=1
        comp1()
        update(flag)
        print("computer win")
        print(flag)
        
        
    if(computer==2):
        flag=2
        comp2()
        update(flag)
        print("you win")
        print(flag)
        
        
    if(computer==3):
        flag = 0
        comp3()
        update(flag)
        print("tie")
        print(flag)
        comp3()


d=turtle.Turtle()
d.penup()
d.goto(-320,-200)
d.pendown()
d.color("gold")
d.write("ENTER [r]-ROCK [s]-STONE [p]-PAPER",font=("Evil Empire",25,"normal"))


def update(flg):
    global cntc
    global cntp
    print("entered update")
    print(flag)
    print(flg)
    print(cntp)
    print(cntc)
    if(flg==0):
        g=turtle.Turtle()
        g.clear()
        g.penup()
        g.goto(-20,-100)
        g.pendown()
        g.color("gold")
        g.write("TIE",font=("Gunplay",25,"normal"))
        time.sleep(1)
        g.undo()

    elif(flg==1):
        cntc=cntc+1
        g=turtle.Turtle()
        g.penup()
        g.goto(-180,-100)
        g.pendown()
        g.color("gold")
        g.write("COMPUTER WON",font=("Gunplay",25,"normal"))
        time.sleep(1)
        g.undo()

    else:
        cntp=cntp+1
        g=turtle.Turtle()
        g.clear()
        g.penup()
        g.goto(-90,-100)
        g.pendown()
        g.color("gold")
        g.write("YOU WON",font=("Gunplay",25,"normal"))
        time.sleep(1)
        g.undo()

    f1=turtle.Turtle()
    f1.penup()
    f1.goto(-300,-300)
    f1.pendown()
    f1.color("gold")
    f1.write("COMPUTER",font=("Crosshatcher",20,"normal"))
    f1.penup()
    f2=turtle.Turtle()
    f2.goto(50,-300)
    f2.pendown()
    f2.color("gold")
    f2.write("PLAYER",font=("Crosshatcher",20,"normal"))
    f3=turtle.Turtle()
    f3.penup()
    f3.goto(-280,-350)
    f3.pendown()
    f3.color("gold")
    f3.write(cntc,font=("verdana",15,"normal"))
    f4=turtle.Turtle()
    f4.penup()
    f4.goto(20,-350)
    f4.pendown()
    f4.color("gold")
    f4.write(cntp,font=("verdana",15,"normal"))
    print("update ended")



def ext():
    quit()



screen.onkey(rock,"r")
screen.onkey(paper,"p")
screen.onkey(scissor,"s")
screen.onkey(ext,"e")
screen.listen()
turtle.done()


