import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

RIGHT=38          # GPIO 13, pin 33
LEFT=40           # GPIO 16, pin 36
REDPIN = 11       # GPIO 17, pin 11
GREENPIN = 12     # GPIO 18, pin 12
BLUEPIN = 13      # GPIO 27, pin 13
BUZZERPIN = 15    # GPIO 22, pin 15
FLAMEPIN = 16     # GPIO 23, pin 16
OBSTACLEPIN = 18  # GPIO 24, pin 18

GPIO.setup(RIGHT, GPIO.IN)
GPIO.setup(LEFT, GPIO.IN)
GPIO.setup(REDPIN, GPIO.OUT)
GPIO.setup(GREENPIN, GPIO.OUT)
GPIO.setup(BLUEPIN, GPIO.OUT)
GPIO.setup(BUZZERPIN, GPIO.OUT)
GPIO.setup(FLAMEPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(OBSTACLEPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#------------Sensor Controls------------------------
def rightSensor():
  return GPIO.input(RIGHT)

def leftSensor():
  return GPIO.input(LEFT)

#------------Buzzer Control-------------------------
#Needs testing, exiting function might stop buzz due to tearing down variable.
#Easy fix, just add global before buzz
def buzzOn():
  buzz = GPIO.PWM(BUZZERPIN, 440)
  buzz.start(50)

def buzzOff():
  buzz = GPIO.PWM(BUZZERPIN)  #Need to 
  buzz.stop()
  GPIO.output(BUZZERPIN, 0)
  
#-------------RGB Controls--------------------------
def redOn():
  GPIO.output(REDPIN, GPIO.HIGH)

def redOff():
  GPIO.output(REDPIN, GPIO.LOW)

def greenOn():
  GPIO.output(GREENPIN, GPIO.HIGH)

def greenOff():
  GPIO.output(GREENPIN, GPIO.LOW)

def blueOn():
  GPIO.output(BLUEPIN, GPIO.HIGH)

def blueOff():
  GPIO.output(BLUEPIN, GPIO.LOW)

def whiteOn():
  GPIO.output(REDPIN, GPIO.HIGH)
  GPIO.output(GREENPIN, GPIO.HIGH)
  GPIO.output(BLUEPIN, GPIO.HIGH)

def blackOn():
  GPIO.output(REDPIN, GPIO.LOW) 
  GPIO.output(GREENPIN, GPIO.LOW)
  GPIO.output(BLUEPIN, GPIO.LOW)

#-----------Flame Detector Controls-----------------
def detectFlame():
  value = GPIO.input(FLAMEPIN)
  return value

#-----------Obstacle detection control--------------
def detectObstacle():
  value = GPIO.input(OBSTACLEPIN)
  return value


