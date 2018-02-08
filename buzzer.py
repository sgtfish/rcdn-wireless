import robotGPIO
import time
import pdb

def buzz(duration):  
  robotGPIO.buzzOn()
  time.sleep(duration)
  robotGPIO.buzzOff()
 
def beep(duration):
  INTERVAL = .5
  while duration > 0:
    #pdb.set_trace()    
    robotGPIO.buzzOn()
    time.sleep(INTERVAL)
    duration = duration - INTERVAL
    robotGPIO.buzzOff()
    if duration <= 0:
      return
    time.sleep(INTERVAL)
    duration = duration - INTERVAL

