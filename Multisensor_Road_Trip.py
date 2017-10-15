#!/usr/bin/python
#
# Pi-Athlon Module 2 - Multisensors Road Trip
# Adds RGB LED, buzzer, obstacle detector, flame/heat detector
#
# Following black line, no obstacle detected -> Green LED
# Detected object -> Stop -> Red LED -> wait 5s -> buzz until obstacle removed -> green LED and proceed forward
# Detected heat >28c -> Stop -> Blue LED -> wait 10s -> ?? wait 10 more seconds ?? -> green LED and proceed forward
#

import RobotInverse
import RobotGPIO
import time

def detectedObstacle():
  RobotGPIO.redOn()
  time.sleep(5)
  RobotGPIO.buzzOn()
  while(RobotGPIO.detectObstacle()):
    #mmm drawing a blank
  RobotGPIO.greenOn()

def detectedFlame():
  RobotGPIO.blueOn()
  time.sleep(20)
  RobotGPIO.greenOn()


