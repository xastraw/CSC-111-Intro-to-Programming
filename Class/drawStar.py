
import turtle


turtle.speed(0)
#turtle.hideturtle()


length = 50
points = 12
evenPoi = points/2

turtle.penup()
#turtle.backward(length/2)
xPos = -length/2
yPos = length/2.75
turtle.setposition(xPos, yPos)
turtle.pendown()

if points % 2 == 0:         #if even number of points
    angle = 180 - 180/evenPoi
    for i in range(int(2*evenPoi)):
        turtle.forward(length)
        turtle.right(angle)
if points % 2 == 1:         #if odd number of points
    angle = 180 - 180/points
    for i in range(points):
        turtle.forward(length)
        turtle.right(angle)

turtle.done()