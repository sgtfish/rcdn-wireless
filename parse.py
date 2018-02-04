import json
import syslogger
import moveRobot

def parseFile(fileName):
  syslogger.log("Parser","INFO","Opening file")
  # This will break if a file is not found. I suggest handling file opening inside a 'try'.
  with open(fileName,'r') as json_file:
    try:
      syslogger.log("Parser","INFO","Begin parsing " + fileName) 
      cmds = json.load(json_file)
      cmd_count = len(cmds)
    except:
      # If we get to this exception, execution will continue on the next 'try'.
      # If we cannot decode the JSON objects from the file, should we continue to compile the commands?
      # Perhaps this can be handled in main, but then something has to be returned here.
      syslogger.log("Parser","ERROR","Could not find JSON objects")
  
    try:
      # This stage suggests that we have the JSON data ready. Is that true?
      # Both "Could not find JSON objects" and "Compiling commands" will get logged. Is that possible? 
      syslogger.log("Parser","INFO","Compiling commands") 
      for i in range(cmd_count):
        action = cmds[i]['action']
        time = cmds[i]['time']

        syslogger.log("Parser","INFO","Sending action " + action + " for " + str(time) + " seconds.")
        moveRobot.command(action,time)
    except:
      syslogger.log("Parser","ERROR","Failed to parse file") 
