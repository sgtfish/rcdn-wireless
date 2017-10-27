import RPi.GPIO as GPIO
import time
import os
import glob
import dht11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

RIGHT=38          # GPIO 13, pin 33
LEFT=40           # GPIO 16, pin 36
REDPIN = 13       # GPIO 27, pin 13
GREENPIN = 15     # GPIO 22, pin 15
BLUEPIN = 16      # GPIO 23, pin 16
BUZZERPIN = 18    # GPIO 24, pin 18
#FLAMEPIN = xx    # GPIO 23, pin 16
OBSTACLEPIN = 22  # GPIO 25, pin 22
#TEMPREAD = 4     # GPIO 4,  pin 7 Assigned in boot/config.txt
DHT11PIN = 11     # GPIO 17, pin 11

GPIO.setup(RIGHT, GPIO.IN)
GPIO.setup(LEFT, GPIO.IN)
GPIO.setup(REDPIN, GPIO.OUT)
GPIO.setup(GREENPIN, GPIO.OUT)
GPIO.setup(BLUEPIN, GPIO.OUT)
GPIO.setup(BUZZERPIN, GPIO.OUT)
#GPIO.setup(FLAMEPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(OBSTACLEPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#------------Sensor Controls------------------------
def rightSensor():
  return GPIO.input(RIGHT)

def leftSensor():
  return GPIO.input(LEFT)

#------------Buzzer Control-------------------------
#Needs testing, exiting function might stop buzz due to tearing down variable.
#Easy fix, just add global before buzz
#buzz = GPIO.PWN(BUZZERPIN, 440)

def buzzOn():
  buzz = GPIO.PWM(BUZZERPIN, 440)
  buzz.start(50)
  time.sleep(2)

def buzzOff():
  buzz = GPIO.PWM(BUZZERPIN)  
  buzz.stop()
  GPIO.output(BUZZERPIN, 0)
  
#-------------RGB Controls--------------------------
def redOn():
  blackOn()
  GPIO.output(REDPIN, GPIO.HIGH)

def redOff():
  GPIO.output(REDPIN, GPIO.LOW)

def greenOn():
  blackOn()
  GPIO.output(GREENPIN, GPIO.HIGH)

def greenOff():
  GPIO.output(GREENPIN, GPIO.LOW)

def blueOn():
  blackOn()
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
#def detectFlame():
#  value = GPIO.input(FLAMEPIN)
#  return value

#-----------DHT11 temp read-------------------------
instance = dht11.DHT11(pin=DHT11PIN)

def read_DHT11_temp():
  result = instance.read()
  return result.temperature

#-----------Temp Read Control-----------------------
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
    #time.sleep(0.2)
    lines = read_temp_raw()
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string) / 1000.0
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c

#-----------Obstacle detection control--------------
def detectObstacle():
  value = GPIO.input(OBSTACLEPIN)
  return value


