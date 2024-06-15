'''A simple two player CAR RACE GAME'''

import turtle
road=turtle.Screen()
road.bgpic("D:\MY DETAILS (THIRU)\LMES\game2\Track.gif")
road.addshape("D:\MY DETAILS (THIRU)\LMES\game2\Bcar.gif")
road.addshape("D:\MY DETAILS (THIRU)\LMES\game2\Rcar.gif")
road.title("++++CAR RACING GAME++++")

redcar=turtle.Turtle()
redcar.setheading(90)
redcar.shape("D:\MY DETAILS (THIRU)\LMES\game2\Rcar.gif")
redcar.penup() 
redcar.goto(-100,-220)

bluecar=turtle.Turtle()
bluecar.setheading(90)
bluecar.shape("D:\MY DETAILS (THIRU)\LMES\game2\Bcar.gif")
bluecar.penup()
bluecar.goto(100,-220)

turtle.listen()

def play1():
    redcar.forward(5)
def play2():
    bluecar.forward(5)

turtle.onkeypress(play1,"Up")
turtle.onkeypress(play2,"w")

while True:
    road.update()
    if redcar.ycor() ==200.00:
        road.bgpic("D:\MY DETAILS (THIRU)\LMES\game2\Redcarwins.gif")
    if bluecar.pos() ==(100.00,200.00):
        road.bgpic("D:\MY DETAILS (THIRU)\LMES\game2\Bluecarwins.gif")

turtle.done()
