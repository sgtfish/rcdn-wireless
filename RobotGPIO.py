import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#Sensor pins
RIGHT=33  # GPIO 13, pin 33
LEFT=36   # GPIO 16, pin 36

#LED pins
REDPIN = 11    # GPIO 17, pin 11
GREENPIN = 12  # GPIO 18, pin 12
BLUEPIN = 13   # GPIO 27, pin 13


GPIO.setup(RIGHT, GPIO.IN)
GPIO.setup(LEFT, GPIO.IN)
GPIO.setup(REDPIN, GPIO.OUT)
GPIO.setup(GREENPIN, GPIO.OUT)
GPIO.setup(BLUEPIN, GPIO.OUT)

def rightSensor():
  return GPIO.input(RIGHT)

def leftSensor():
  return GPIO.input(LEFT)

