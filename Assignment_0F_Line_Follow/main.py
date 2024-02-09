#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

leftmotor = Motor(Port.B)
rightmotor = Motor(Port.C)

robot = DriveBase(leftmotor, rightmotor, wheel_diameter=56, axle_track=104)

blacksense = ColorSensor(Port.S4)
colorsense = ColorSensor(Port.S1)


mywatch = StopWatch()
# Write your program here.
white = 30  
black = 7
threshold = 16#(white + black) / 2


kp = 4.5#4.8#4.2#2
kd = .009#.009#0.01#.2
ki = .005#0.008#.01


integral = 0
derivative = 0
last_error = 0
redvar = 0  #variable to make it so when the robot stops on red, it only goes through red and stops once


mywatch.reset()
mywatch.pause()

while True:

    startingtime = mywatch.time()

    speed_color = colorsense.color()
    reflect = blacksense.reflection()

    error = reflect - threshold
    integral = integral + error
    derivative = error - last_error

    turn_rate = (kp * error) + (ki * integral) + (kd * derivative)
    
    if speed_color == Color.YELLOW:
        robot.drive(40, turn_rate)
        mywatch.resume()
        redvar = 0
 
    elif speed_color == Color.GREEN:
        robot.drive(80, turn_rate)
        redvar = 0
    
    elif speed_color == Color.RED:
        if redvar == 0:
            robot.stop()
            redvar = 1
            wait(3000)
            startingtime += 3000
        robot.drive(30, turn_rate)
    
    elif speed_color == Color.BLUE:       
        
        if startingtime > 0:
            mywatch.pause()
            robot.stop()
            break

        robot.drive(40, turn_rate)
        redvar = 0


    last_error = error

print(startingtime)