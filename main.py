#!/usr/bin/python
#
import time
import pid
import RobotInverse
import RobotGPIO
import Multisensor_Road_Trip as Module2
import os
import pdb


def main():
  LEFT_TRIM  = -1
  RIGHT_TRIM = -5
  INIT_SPEED = 175
  
  error_previous = 0
  i = 0
  lSpeed = INIT_SPEED
  rSpeed = INIT_SPEED
  
  robot = RobotInverse.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)  
  RobotGPIO.greenOn()
  pid.setMotorSpeeds(lSpeed, rSpeed)

  while(1):
    lSpeed, rSpeed = pid.runPID(INIT_SPEED, error_previous, i)

if __name__ == '__main__':

   main()
