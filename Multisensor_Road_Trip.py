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
import os
import glob

def detectedObstacle():
  Obstacle_Detected = False
  RobotGPIO.redOn()
  time.sleep(5)
  RobotGPIO.buzzOn()
  while(Obstacle_Detected == True):
    #mmm drawing a blank
    if not RobotGPIO.detectObstacle():
      # Returns 1 if obsatcle detected
      Obstacle_Detected = False
  RobotGPIO.greenOn()

#-----------Temp Read-----------------------------
# Used this for reference
# Still need to do inital config, see link below
# https://cdn-learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf
#

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

def read_temp():
  lines = read_temp_raw()
  while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = read_temp_raw() 
  equals_pos = lines[1].find('t=') 
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:] 
    temp_c = float(temp_string) / 1000.0 
    temp_f = temp_c * 9.0 / 5.0 + 32.0 
    return temp_c, temp_f

---------------------------------------------------

def detectedFlame():
  RobotGPIO.blueOn()
  time.sleep(20)
  RobotGPIO.greenOn()


