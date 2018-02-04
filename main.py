#!/usr/bin/python
#
import time
import robotInverse
import robotGPIO
import Multisensor_Road_Trip as Module2
import os
import pdb
import SpinningPumpkin

# Trim:
# Negative value slows down the motor
LEFT_TRIM   = -1
RIGHT_TRIM = -5

# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
robot = RobotInverse.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)


def main():
  

if __name__ == '__main__':
  main()
