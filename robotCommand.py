import robotGPIO
import robotInverse
import buzzer
import led
import pdb
import syslogger

# Trim:
# Negative value slows down the motor
LEFT_TRIM   = -1
RIGHT_TRIM = -5

robot = robotInverse.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
SPEED = 100

FACILITY = "robotCommand.py"

def command(action, duration):
  #pdb.set_trace()
  if action == "forward":
    syslogger.log(FACILITY, "INFO", "Moving robot forward for " +str(duration)+ " seconds.")
    robot.forward(SPEED, duration)

  elif action == "backward":
    syslogger.log(FACILITY, "INFO", "Moving robot backward for " +str(duration)+ " seconds.")
    robot.backward(SPEED, duration)

  elif action == "left":
    syslogger.log(FACILITY, "INFO", "Turning robot left for " +str(duration)+ " seconds.")
    robot.leftTurn(SPEED, duration)

  elif action == "right":
    syslogger.log(FACILITY, "INFO", "Turning robot right for " +str(duration)+ " seconds.")
    robot.rightTurn(SPEED, duration)

  elif action == "play_sound":
    #pdb.set_trace()
    syslogger.log(FACILITY, "INFO", "Playing sound for " +str(duration)+ " seconds.")
    #robotGPIO.buzzOn(duration)    
    buzzer.buzz(duration)

  elif action == "led_blue":
    syslogger.log(FACILITY, "INFO", "Blue LED for " +str(duration)+ " seconds.")
    led.blue(duration)

  elif action == "led_green":
    syslogger.log(FACILITY, "INFO", "Green LED " +str(duration)+ " seconds.")
    led.green(duration)

  elif action == "led_red":
    syslogger.log(FACILITY, "INFO", "Red LED for " +str(duration)+ " seconds.")
    led.red(duration)

  elif action == "stop":
    #pdb.set_trace()
    syslogger.log(FACILITY, "INFO", "Stopping robot activity for " +str(duration)+ " seconds.")
    robot.stop(SPEED, duration)

  else:
    #pdb.set_trace()
    syslogger.log(FACILITY, "ERROR", "Action not found!")
    robotGPIO.redOn() # manually interfacing red LED via robotGPIO to multitask LED and buzzer activity, as standard definition uses time.sleep command
    buzzer.beep(5)
    robotGPIO.redOff()
  return

