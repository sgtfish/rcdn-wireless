import robotGPIO
import time

def buzz(duration):
  robotGPIO.buzzOn()
  time.sleep(duration)
  robotGPIO.buzzOff()
 
def beep(duration):
  INTERVAL = 0.25
  while duration > 0:
    robotGPIO.buzzOn()
    time.sleep(INTERVAL)
    duration = duration - INTERVAL
    robotGPIO.buzzOff()
    time.sleep(INTERVAL)
    duration = duration - INTERVAL
