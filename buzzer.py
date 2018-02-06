import robotGPIO
import time

def buzz(duration):
  robotGPIO.buzzOn()
  time.sleep(duration)
  robotGPIO.buzzOff()
 
def beep(duration):
  INTERVAL = 0.25
  while duration > 0:
    buzzOn()
    time.sleep(INTERVAL)
    duration = duration - INTERVAL
    buzzOff()
    time.sleep(interval)
    duration = duration - INTERVAL
