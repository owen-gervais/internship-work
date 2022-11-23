#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import ubinascii, ujson, urequests, utime

Key = 'd_sQ3N4rGP7ss3xmbUt5ti_SuBIkzploxOcNaFTUGe'

def SL_setup():
     urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     headers = {"Accept":"application/json","x-ni-api-key":Key}
     return urlBase, headers

def Put_SL(Tag, Type, Value):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     propValue = {"value":{"type":Type,"value":Value}}
     try:
          reply = urequests.put(urlValue,headers=headers,json=propValue).text
     except Exception as e:
          print(e)         
          reply = 'failed'
     return reply

def Get_SL(Tag):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          #print(data)
          result = data.get("value").get("value")
     except Exception as e:
          print(e)
          result = 'failed'
     return result


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
#ev3.speaker.beep()
colorsensor = ColorSensor(Port.S4)


ev3.buttons.pressed()

while True:
    buttonPress = ev3.buttons.pressed()
    if len(buttonPress) > 0:
        rgb = colorsensor.rgb()
        rVal = rgb[0]
        gVal = rgb[1]
        bVal = rgb[2]
        if rVal > gVal and rVal > bVal:
            Put_SL('color','STRING', 'red')
        elif gVal > bVal and gVal > rVal:
            Put_SL('color','STRING','green')
        elif bVal > gVal and bVal > rVal:
            Put_SL('color','STRING','blue')
        print('I posted the new color!')
    print('Waiting for input....')
    wait(1000)
    


