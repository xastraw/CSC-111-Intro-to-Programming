
import turtle
from math import pi
import random
from StrawTurtleLibrary import *
import time



name = input("What do you want the name of the turtle to be? ")
name = turtle.Turtle()

def drawStar():

    xx = int(input("What x-coordinate do you want the center to be at for the star? "))
    yy = int(input("What y-coordinate do you want the center to be at for the star? "))
    starPoints = int(input("How many points do you want the star to have? "))
    starLength = int(input("How long do you want each length of the star to be? "))

    turtleStar(xx, yy, starLength, starPoints, name)

def drawPoly():
    xxx = int(input("What x-coordinate do you want the center to be at for the polygon? "))
    yyy = int(input("What y-coordinate do you want the center to be at for the polygon? "))
    polyPoints = int(input("How many points do you want the polygon to have? "))
    polyLength = int(input("How long do you want each side of the polygon to be? "))

    turtlePloygon(xxx, yyy, polyLength, polyPoints, name)


def drawArt():
    xxxx = int(input("What x-coordinate do you want the center to be at for the turtle art? "))
    yyyy = int(input("What y-coordinate do you want the center to be at for the turtle art? "))
    artCircle = int(input("What do you want the radius of the circles for the art to be? "))
    iterations = int(input("How many circles do you want? "))

    turtleArt(xxxx, yyyy, artCircle, iterations, name)



def main():

    
    
    turtle.colormode(255)
    
    star = input("Do you want to draw a star? Yes/No ")
    poly = input("Do you want to draw a polygon? Yes/No ")
    art = input("Do you want to draw art? Yes/No ")

    screen = turtle.Screen()

    if(star == 'Yes' or star == 'yes'):
        drawStar()
    if(poly == 'Yes' or poly == 'yes'):
        drawPoly()
    if(art == 'Yes' or art == 'yes'):
        drawArt()

    
    
    turtle.exitonclick()

main()


