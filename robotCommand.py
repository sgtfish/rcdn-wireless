mport robotGPIO
import robotInverse
import buzzer
import led
import pdb


# Trim:
# Negative value slows down the motor
LEFT_TRIM   = -1
RIGHT_TRIM = -5

robot = robotInverse.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
SPEED = 100

FACILITY = "robotCommand.py"

def command(action, duration):
  if action == "forward":
    syslogger.log(FACILITY, "INFO", "Moving robot forward for " +duration+ " seconds.")
    robot.forward(SPEED, duration)

  elif action == "backward":
    syslogger.log(FACILITY, "INFO", "Moving robot backward for " +duration+ " seconds.")
    robot.backward(SPEED, duration)

  elif action == "left":
    syslogger.log(FACILITY, "INFO", "Turning robot left for " +duration+ " seconds.")
    robot.leftTurn(SPEED, duration)

  elif action == "right":
    syslogger.log(FACILITY, "INFO", "Turning robot right for " +duration+ " seconds.")
    robot.rightTurn(SPEED, duration)

  elif action == "play_sound":
    syslogger.log(FACILITY, "INFO", "Playing sound for " +duration+ " seconds.")
    buzzer.buzz(duration)

  elif action == "led_blue":
    syslogger.log(FACILITY, "INFO", "Blue LED for " +duration+ " seconds.")
    led.blue(duration)

  elif action == "led_green":
    syslogger.log(FACILITY, "INFO", "Green LED " +duration+ " seconds.")
    led.green(duration)

  elif action == "led_red":
    syslogger.log(FACILITY, "INFO", "Red LED for " +duration+ " seconds.")
    led.red(duration)

  elif action == "stop":
    syslogger.log(FACILITY, "INFO", "Stopping robot activity for " +duration+ " seconds.")
    robot.stop(SPEED, duration)

  else:
    syslogger.log(FACILITY, "ERROR", "Action not found!")
    robotGPIO.redOn() # manually interfacing red LED via robotGPIO to multitask LED and buzzer activity, as standard definition uses time.sleep command
    buzzer.beep(5)
    robotGPIO.redOff()

