#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from math import sin, cos, pi


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.beep()

# Conversion from degrees to radians
deg_2_rad = pi/180

# Initialize all of the peripherals
leftMotor = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
ultra = UltrasonicSensor(Port.S1)

# Rotation and speed of the robot
rotation_angle = 8
speed = 300

# Create all of the points
point_x = []
point_y = []

lower = 0
upper = 365
length = 146
headings = [lower + x*(upper-lower)/length for x in range(length)]
for i in range(length):
    rightMotor.run_angle(speed, rotation_angle, then=Stop.HOLD, wait=False)
    leftMotor.run_angle(speed, -rotation_angle, then=Stop.HOLD, wait=True)
    dist = ultra.distance()
    point_x.append(dist*cos(headings[i]*deg_2_rad))
    point_y.append(dist*sin(headings[i]*deg_2_rad))

print(point_x)
print("--------")
print(point_y)