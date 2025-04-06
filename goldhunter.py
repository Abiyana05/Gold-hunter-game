import turtle
import random

score=0

sea=turtle.Screen()
sea.bgpic("sea.gif")
sea.addshape("left.gif")
sea.addshape("right.gif")
sea.addshape("coin.gif")

hunter=turtle.Turtle()
hunter.shape("left.gif")
hunter.penup()
hunter.goto(0,-150)

coin=turtle.Turtle()
coin.speed(1000)
coin.shape("coin.gif")
coin.penup()
coin.goto(-280,280)

scoreboard=turtle.Turtle()
scoreboard.penup()
scoreboard.goto(-100,240)
scoreboard.write("score:0",font=("courier",27,"bold"))
scoreboard.hideturtle()
scoreboard.speed(500)

def right():
    hunter.shape("right.gif")
    hunter.forward(5)

def left():
    hunter.shape("left.gif")
    hunter.backward(5)    

turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()
#coin should fall so increase the y axis
def move():
    y=coin.ycor()#to find y cordinate
    coin.sety(y-3)#to set the y axis

while True:
    sea.update()
    move()
    #if the coin reaches down then itshould start from the begining from random x axis
    if coin.ycor() < -300:
        x=random.randint(-280,280)
        coin.goto(x,280)
    if hunter.distance(coin) < 50:
       score=score+1
       scoreboard.clear() #to clear the initial assigned 0 value
       scoreboard.write("score:{}".format(score),font=("courier",27,"bold"))
       x=random.randint(-280,280)
       coin.goto(x,280)     


turtle.done()