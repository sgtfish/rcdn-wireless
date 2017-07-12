import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

RIGHT=33  # GPIO 13, pin 33
LEFT=36   # GPIO 16, pin 36

GPIO.setup(RIGHT, GPIO.IN)
GPIO.setup(LEFT, GPIO.IN)

def rightSensor():
  return GPIO.input(RIGHT)

def leftSensor():
  return GPIO.input(LEFT)

