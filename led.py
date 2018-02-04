import robotGPIO
import time

def blue(duration):
  robotGPIO.blueOn()
  time.sleep(duration)
  robotGPIO.blueOff()
  
def green(duration):
  robotGPIO.greenOn()
  time.sleep(duration)
  robotGPIO.greenOff()
  
def red(duration):
  robotGPIO.redOn()
  time.sleep(duration)
  robotGPIO.redOff()
