#!/usr/bin/python
#
import time
import RobotInverse
import RobotGPIO
import Multisensor_Road_Trip as Module2
import pdb

# Trim:
# Negative value slows down the motor
LEFT_TRIM   = 0
RIGHT_TRIM  = -4


# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
robot = RobotInverse.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)


# Return the concatonated values of the sensor inputs (number of possible states == 2^(number_of_sensors)-1)
def sensorRead():
  L = RobotGPIO.leftSensor()
  R = RobotGPIO.rightSensor()
  return str(L)+str(R)

# Return the positive or negative error value, dependent upon the current state of the sensors
# Positive value == Turn Left
# Negative value == Turn Right
def errorEval(variable, ERROR_PREVIOUS):
  array = ['10','11','01']
  try:
    index = array.index(variable)
  except:
    if ERROR_PREVIOUS < 0:
      error = (len(array)-1)*-1
      return error
    else:
      error = (len(array)-1)
      return error 
  error = index - ((len(array)-1)/2)  # calculate the error based upon the size of the array
  return error


# "Nonlinear: interpretation of error
# Positive value == Turn Left
# Negative value == Turn Right
def errorEval2(variable, ERROR_PREVIOUS):
  array = ['10','11','01']
  if variable == '10':
    error = -1
  elif variable == '11':
    error = 0
  elif variable == '01':
    error = 1
  elif variable == '00':
    if ERROR_PREVIOUS < 0:
      error = -4.5
    else:
      error = 4.5
  return error
    
def calculatePID(ERROR, ERROR_PREVIOUS, I):
  Kp = 50
  Ki = .15
  Kd = 60
  P = ERROR
  I =  I + ERROR
  D = ERROR - ERROR_PREVIOUS
  if I > 255:
    I = 255
  elif I < -255:
    I = -255
  PIDvalue = (Kp*P) + (Ki*I) + (Kd*D)
  print "P: %s   I: %s   D: %s   PIDvalue: %s" % (P,I,D,PIDvalue)
  return int(round(PIDvalue,0)), I

def setMotorSpeeds(LSPEED, RSPEED):
  #print "LSPEED: %s    RSPEED: %s" % (LSPEED,RSPEED)
  if (LSPEED > 255) or (LSPEED < -255) or (RSPEED > 255) or  (RSPEED < -255):
    pdb.set_trace()  
  if LSPEED >= 0:
    try:
      robot.leftPID(LSPEED)
    except:
      x = 1
      #pdb.set_trace()
      #print '=== FORWARD LEFT EXCEPTION ==='
  else:
    try:
      robot.leftPIDreverse(-1*LSPEED)
    except:
      x = 1
      #pdb.set_trace()
      #print '=== REVERSE LEFT EXCEPTION ==='
  if RSPEED >= 0:
    try:
     robot.rightPID(RSPEED)
    except:
      x = 1
      #pdb.set_trace()
      #print '=== FORWARD RIGHT EXCEPTION ==='
  else:
    try:
      robot.rightPIDreverse(-1*RSPEED)
    except:
      x = 1
      #pdb.set_trace()
      #print '=== REVERSE RIGHT EXCEPTION ==='
  return 



# Speed is limited to 255 as defined by the motor drivers
# If the determined speed is found to exceed 255, we need to not only cap the speed to 255 for the relevant motor,
# but also take the difference and apply it to the opposing motor in order to maintain the severity of turns
def scaleSpeed(LSPEED, RSPEED):
  SCALE_FLAG = False
  if LSPEED > 255:
    RSPEED = RSPEED - (LSPEED-255)
    LSPEED = 255
    SCALE_FLAG = True
  elif LSPEED < -255:
    RSPEED = RSPEED - (LSPEED-(-255))
    LSPEED = -255
    SCALE_FLAG = True
  if RSPEED > 255:
    if SCALE_FLAG == False:
      LSPEED = LSPEED - (RSPEED-255)
      RSPEED = 255
    else:
      RSPEED = 255
  elif RSPEED < -255:
    if SCALE_FLAG == False:
      LSPEED = LSPEED - (LSPEED-(-255))
      RSPEED = -255
    else:
      RSPEED = -255
  return LSPEED,RSPEED

def main():
  INIT_SPEED = 150
  ERROR_PREVIOUS = 0
  I = 0
  while(1):
    ERROR = errorEval2(sensorRead(), ERROR_PREVIOUS)
    PIDvalue, I = calculatePID(ERROR, ERROR_PREVIOUS, I)
    if PIDvalue != ERROR_PREVIOUS:
      LSPEED = INIT_SPEED - PIDvalue
      RSPEED = INIT_SPEED + PIDvalue
      LSPEED, RSPEED = scaleSpeed(LSPEED, RSPEED)
      LSPEED, RSPEED = scaleSpeed(LSPEED, RSPEED)
      setMotorSpeeds(LSPEED, RSPEED)
    
    #if(RobotGPIO.detectFlame() == 1):
       #setMotorSpeeds(0,0)
       #Module2.detectedFlame()
       #setMotorSpeeds(LSPEED, RSPEED)

    #if(RobotGPIO.detectObstacle() == 1):
       #setMotorSpeeds(0,0)
       #Module2.detectedObstacle()
       #setMotorSpeeds(LSPEED, RSPEED)

    ERROR_PREVIOUS = ERROR

if __name__ == '__main__':

  main()
