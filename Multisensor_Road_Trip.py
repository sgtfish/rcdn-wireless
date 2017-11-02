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
import RPi.GPIO as GPIO
import time
import os
import glob
import pdb

GPIO.setmode(GPIO.BOARD)

def detectedObstacle():
  RobotGPIO.redOn()
  time.sleep(5)
  #RobotGPIO.buzzOn()
  buzz = GPIO.PWM(18, 440)
  buzz.start(50)
  while(RobotGPIO.detectObstacle() == 0):
    Obstacle_Detected = True  # Don't go anywhere if there's still an obstacle in the way after waiting 5 seconds
  buzz.stop()
  RobotGPIO.redOff()
  RobotGPIO.greenOn()

def detectedHighTemp():
  #pdb.set_trace()
  RobotGPIO.blueOn()
  time.sleep(20)
  RobotGPIO.blueOff()
  RobotGPIO.greenOn()

def detectedFlame():
  RobotGPIO.whiteOn()
  buzzTone = 300
  up = True
  pdb.set_trace()
  buzz = GPIO.PWM(18, 300)
  buzz.start(50)
  while(RobotGPIO.detectFlame() == 1):
    time.sleep(.05)
    print buzzTone
    if buzzTone == 500:
      up = False
    if buzzTone == 300:
      up = True
    if buzzTone < 500 and up:
      buzzTone = buzzTone + 10
    if buzzTone > 300 and not up:
      buzzTone = buzzTone - 10
    buzz.ChangeFrequency(buzzTone)
    #buzz.start(50)
  buzz.stop()
  #print "Buzz Stop"
  RobotGPIO.blackOn()
  RobotGPIO.greenOn()

def detectedTilt():
  tilted = True
  while(tilted):
    RobotGPIO.blueOn()
    time.sleep(.2)
    RobotGPIO.greenOn()
    time.sleep(.2)
    RobotGPIO.redOn()
    time.sleep(.2)
    print RobotGPIO.detectTilt()
    if(RobotGPIO.detectTilt() == 0):
      tilted = False
  RobotGPIO.blackOn()
  RobotGPIO.greenOn()
