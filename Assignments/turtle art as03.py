import turtle
import random 

height = 500
width = 500
screen = turtle.Screen()
screen.setup(width, height)                     #screen is total of 500, so from -250 to 250 on both x and y
screen.bgcolor("black")



turtle.colormode(255)
alex = turtle.Turtle()

alex.color("white")
alex.speed(0)


alex.penup()
alex.backward(50)       #center the drawing
alex.left(90)
alex.pendown()



def main():
    for i in range (60):
        
        r,g,b= random.randint(0,255), random.randint(0,255), random.randint(0,255)
        alex.pencolor((r,g,b))
        

        alex.circle(20+i**1.2)       #left circle
        alex.right(45)
        alex.penup()
        alex.forward(50)
        alex.pendown()
        alex.setheading(0)

        alex.circle(20+i**1.2)       #top circle
        alex.right(45)
        alex.penup()
        alex.forward(50)
        alex.setheading(270)
        alex.pendown()

        alex.circle(20+i**1.2)       #right circle
        alex.penup()
        alex.right(45)
        alex.forward(50)
        alex.pendown()
        alex.setheading(180)

        alex.circle(20+i**1.2)      #bottom circle
        alex.right(45)
        alex.penup()
        alex.forward(50)
        alex.pendown()
        alex.setheading(90)



main()


turtle.exitonclick()