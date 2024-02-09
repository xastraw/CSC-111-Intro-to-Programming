
import turtle
from LSystemLibrary import *


axe = "FB"

baseRule1 = "F"
baseRule2 = "B"
rule1 = "F+B"
rule2 = "F-B"

def main():
    iterations = int(input("How many iterations would you like (At least 0)? "))
    color = str(input("What color would you like it to be? "))

    screen = turtle.Screen()
    screen.bgcolor("black")
    alex = turtle.Turtle()
    
    turtle.tracer(0, 0)
    alex.up()
    alex.setposition(200, 50)
    alex.down()

    DrawLSystem(alex, color, ApplyLSystem(axe, baseRule1, baseRule2, rule1, rule2, iterations))

    alex.hideturtle()
    turtle.update()

main()



turtle.exitonclick()
