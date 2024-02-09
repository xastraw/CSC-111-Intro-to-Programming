
import math


def TurtleDrawPolygon(radius, numsides, theturtle):

    angle = 360/numsides


    edge = radius*(2*math.sin((angle/2)*(math.pi/180)))

    print("radius is:",radius)
    print(("edge:",edge))

    theturtle.up()
    theturtle.forward(radius)
    theturtle.down()
    theturtle.left(90+angle/2)

    for i in range(0, numsides):
        theturtle.forward(edge)
        theturtle.left(angle)