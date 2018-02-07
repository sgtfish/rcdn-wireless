import json
import syslogger
import robotCommand
import sys
import pdb

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
    #pdb.set_trace()
    syslogger.log(FACILITY,"INFO","Compiling commands")
    for i in range(cmd_count):
      action = cmds[i]['action']
      time = cmds[i]['time']

      syslogger.log(FACILITY,"INFO","Sending action " + action + " for " + str(time) + " seconds.")
      robotCommand.command(action,time)
  except:
    syslogger.log(FACILITY,"ERROR","Failed to parse file")
    sys.exit(1)
