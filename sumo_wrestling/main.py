#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

leftmotor = Motor(Port.A)
rightmotor = Motor(Port.B)

robot = DriveBase(leftmotor, rightmotor, wheel_diameter=56, axle_track=104)

flipsensor = Motor(Port.C)
rearsensor = ColorSensor(Port.S2)
frontsensor = ColorSensor(Port.S1)
sonic = UltrasonicSensor(Port.S4)

while True:
    if Button.CENTER in ev3.buttons.pressed():
        break
    else:
        pass
wait(5000)
# Write your program here.

robot.settings(300,300,200)

robot.drive(150,0)

while True:

    front_board_color = frontsensor.color()
    rear_board_color = rearsensor.color()
    dist = sonic.distance(False)
    print(dist)
    flipsensor.run_target(100, 0)

    if(front_board_color) == Color.WHITE:
        robot.straight(-75)
        robot.stop()
        robot.turn(180)
        robot.drive(150,0)

    if(rear_board_color) == Color.WHITE:
        robot.drive(250,0)
    
    if dist < 120:
        robot.drive(350,0)
        flipsensor.run_target(100, 50)
    if dist < 300:
        robot.drive(250,0)
    
    if dist > 300:
        robot.drive(150,0)
    
    

        
    #dist < 300 speed up
    #dist < 120 very fast