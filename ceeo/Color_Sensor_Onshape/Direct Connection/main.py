#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import os

'''
    EV3 Color Sensor Detection and Onshape API Connection Main:

    The purpose of the below code is to establish communication between
    the EV3 Color Sensor and Onshape API. The color is stored and then 
    formatted using the below dictionary and a command line prompt using the
    os library. Due to this file running on micropython, the path to the usr/bin
    must be established so that it can be run.
'''

# Initializing the Color Sensor on the EV3
colorsensor = ColorSensor(Port.S4)

# Color Dictionary correlates the name with RGB array
colorDict = {'red':[255,0,0], 'green':[0,255,0], 'blue':[0,0,255]}

# Initializing the ev3 class instance
ev3 = EV3Brick()

color = ''

# The below loop waits for user input and assigns the detected color 
while True:
    buttonPress = ev3.buttons.pressed()
    if len(buttonPress) > 0:
        rgb = colorsensor.rgb()
        rVal = rgb[0]
        gVal = rgb[1]
        bVal = rgb[2]
        if rVal > gVal and rVal > bVal:
            color = 'red'
        elif gVal > rVal and gVal > bVal:
            color = 'blue'
        elif bVal > rVal and bVal > gVal:
            color = 'green'
        print('Color Sensor Detected: ' + color)
        break
    print('Waiting for user input')
    wait(1000)

# Command formats the command line prompt for later call
command = 'python3.5 onshapeCommunication.py ' + str(colorDict[color][0]) + " " + str(colorDict[color][1]) + " " + str(colorDict[color][2])

# os runs the Onshape API with outside script
print('Onshape API Communication: Running....')
os.system(command)


