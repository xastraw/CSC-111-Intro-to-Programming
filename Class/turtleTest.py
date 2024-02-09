import turtle
import math


numsides = 7
angle = 360/numsides
radius = 100

#compute ployygon radius in terms of edge length
#r = d/(2sin(theta/2))


edge = radius * (2*math.sin((angle/2)*(math.pi/180)))
print("radius is:", edge)

screen = turtle.Screen()
alex = turtle.Turtle()


alex.up()
alex.forward(radius)
alex.down()
alex.left(90+angle/2)

for i in range(0, numsides):
    alex.left(angle)
    alex.forward(edge)


turtle.done()