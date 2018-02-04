import robotGPIO
import time

def buzz(duration):
  robotGPIO.buzzOn()
  time.sleep(duration)
  robotGPIO.buzzOff()
 
