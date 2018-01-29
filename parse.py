import json
import syslogger
import moveRobot

def parseFile(fileName):
  syslogger.log("Parser","INFO","Opening file")
  with open(fileName,'r') as json_file:
    try:
      syslogger.log("Parser","INFO","Begin parsing " + fileName) 
      cmds = json.load(json_file)
      cmd_count = len(cmds)
    except:
      syslogger.log("Parser","ERROR","Could not find JSON objects")
  
    try:
      syslogger.log("Parser","INFO","Compiling commands")
      for i in range(cmd_count):
        action = cmds[i]['action']
        time = cmds[i]['time']

        syslogger.log("Parser","INFO","Sending action " + action + " for " + str(time) + " seconds.")
        moveRobot.command(action,time)
    except:
      syslogger.log("Parser","ERROR","Failed to parse file")
