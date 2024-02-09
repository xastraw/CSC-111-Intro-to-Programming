
from math import pi
import random


def turtleStar(xCor, yCor, leng, points, theTurtle):

    theTurtle.up()
    xPos = xCor - leng/2
    yPos = yCor + leng/2.75
    #theTurtle.backward(leng/2)
    theTurtle.setpos(xPos, yPos)
    theTurtle.down()

    evenPoints = points/2           #this formula creates a half of however many points there are so need to divide it
    if points % 2 == 0:     #if the star points are even
        angle = 180 - 180/evenPoints
        for i in range(int(2*evenPoints)):
            theTurtle.forward(leng)
            theTurtle.right(angle)
    if points % 2 == 1:
        angle = 180 - 180/points
        for i in range(points):
            theTurtle.forward(leng)
            theTurtle.right(angle)
    




def turtlePloygon(xCor, yCor, leng, points, theTurtle):
    
    theTurtle.speed(0)

    #theTurtle.up()
    posX = xCor - leng/2
    posY = yCor + leng * points/(2*pi)
    theTurtle.setposition(posX, posY)
    theTurtle.backward(leng/2)
    theTurtle.down()


    for i in range(points):
        theTurtle.forward(leng)
        theTurtle.right(360/points)



def turtleArt(posX, posY, circleSize,numIterations, theTurtle):

    theTurtle.up()
    theTurtle.setpos(posX, posY)
    theTurtle.down()
    theTurtle.color("white")
    theTurtle.speed(0)


    theTurtle.penup()
    theTurtle.backward(50)       #center the drawing
    theTurtle.left(90)
    theTurtle.pendown()

    for i in range (0, numIterations):
        
        r,g,b= random.randint(0,255), random.randint(0,255), random.randint(0,255)
        theTurtle.pencolor((r,g,b))
        

        theTurtle.circle(circleSize+i**1.2)       #left circle
        theTurtle.right(45)
        theTurtle.penup()
        theTurtle.forward(circleSize*2)
        theTurtle.pendown()
        theTurtle.setheading(0)

        theTurtle.circle(circleSize+i**1.2)       #top circle
        theTurtle.right(45)
        theTurtle.penup()
        theTurtle.forward(circleSize*2)
        theTurtle.setheading(270)
        theTurtle.pendown()

        theTurtle.circle(circleSize+i**1.2)       #right circle
        theTurtle.penup()
        theTurtle.right(45)
        theTurtle.forward(circleSize*2)
        theTurtle.pendown()
        theTurtle.setheading(180)

        theTurtle.circle(circleSize+i**1.2)      #bottom circle
        theTurtle.right(45)
        theTurtle.penup()
        theTurtle.forward(circleSize*2)
        theTurtle.pendown()
        theTurtle.setheading(90)

