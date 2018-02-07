import json
import syslogger
import robotCommand
import sys

FACILITY = "parse.py"

def parseFile(fileName):
  syslogger.log(FACILITY,"INFO","Opening file")
  try:
    with open(fileName,'r') as json_file:
      try:
        syslogger.log(FACILITY,"INFO","Begin parsing " + fileName)
        cmds = json.load(json_file)
        cmd_count = len(cmds)
      except:
        syslogger.log(FACILITY,"ERROR","Could not find JSON objects")
        sys.exit(1)
  except:
    syslogger.log(FACILITY,"ERROR","File not found in flash!")
    sys.exit(1)

  try:
    syslogger.log(FACILITY,"INFO","Compiling commands")
    for i in range(cmd_count):
      action = cmds[i]['action']
      duration = cmds[i]['duration']

      syslogger.log(FACILITY,"INFO","Sending action " + action + " for " + str(duration) + " seconds.")
      robotCommand.command(action,duration)
  except:
    syslogger.log(FACILITY,"ERROR","Failed to parse file")
    sys.exit(1)
