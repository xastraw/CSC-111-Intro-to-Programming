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
rightmotor = Motor(Port.C)
leftmotor = Motor(Port.B)
robot = DriveBase(leftmotor, rightmotor, wheel_diameter=56, axle_track=112)



# Write your program here.

robot.straight(1000)#drives 1 meter forward
robot.straight(-1000)
robot.turn(1080)

rightmotor.run_target(1000, 1440)

for i in range(4):
    robot.straight(500)
    robot.turn(90)

