import json
import syslogger
import robotCommand

def parseFile(fileName):
  syslogger.log("Parser","INFO","Opening file")
  try:
    with open(fileName,'r') as json_file:
      try:
        syslogger.log("Parser","INFO","Begin parsing " + fileName)
        cmds = json.load(json_file)
        cmd_count = len(cmds)
      except:
        syslogger.log("Parser","ERROR","Could not find JSON objects")
        sys.exit(1)
  except:
    syslogger.log("Parser","ERROR","File not found in flash!")
    sys.exit(1)
  
  try:
    syslogger.log("Parser","INFO","Compiling commands") 
    for i in range(cmd_count):
      action = cmds[i]['action']
      duration = cmds[i]['duration']

      syslogger.log("Parser","INFO","Sending action " + action + " for " + str(duration) + " seconds.")
      robotCommand.command(action,duration)
  except:
    syslogger.log("Parser","ERROR","Failed to parse file") 
    sys.exit(1)
