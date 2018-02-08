#!/usr/bin/python
import time
import robotInverse
import robotGPIO
import os
import pdb
import download
import parse
import syslogger
import sys
import argparse
import json

#FTP - Requires no directory input = ""
#HTML - Requires '/' for directory
#SSH - Requires full pwd for directory

settings_file = "settings.json"

def main(downloadMethod, ip, username, password, directory, fileName):
  #downloadMethod = "ssh"
  #ip = "10.154.66.159"
  #directory = "/home/pi/sftp/"
  #username = "pi"
  #password = "raspberry"
  #fileName = "actions.json"

  download.downloadFile(downloadMethod, ip, directory, username, password, fileName)  

  #if(downloadMethod == "ssh"):
  #  print "Entering ssh download"
  #  download.ssh(ip,directory,username,password,fileName)
  #elif(downloadMethod == "ftp"):
  #  print "Entering ftp download"
  #  download.ftp(ip,directory,username,password,fileName)
  #elif(downloadMethod == "html"):
  #  print "Entering html download"
  #  download.html(ip,directory,username,password,fileName)
  #else:
  #  syslogger.log("Main","ERROR","Invalid download method")
  #  sys.exit(1)

  parse.parseFile(fileName)
  return


if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument("downloadMethod", help="The download method to use (ssh, ftp, or html)")

  args = parser.parse_args()
    
  downloadMethod = args.downloadMethod
  
  if downloadMethod not in ["ssh", "ftp", "html"]:
      print "error: invalid download method: " + downloadMethod
      sys.exit(1)
  
  # getting the rest of the config from file
  try:
    with open(settings_file, "r") as f:
      try:
	#pdb.set_trace()
        settings = json.load(f)
        # pdb.set_trace()
        # server settings
        ip = settings[0]["server"]["ip"]
        username = settings[0]["server"]["username"]
        password = settings[0]["server"]["password"]
        fileName = settings[0]["server"]["fileName"]
        
        # directory settings (ssh, ftp, or http)
        if downloadMethod == "ssh":
          directory = settings[1]["directories"]["ssh"]
        elif downloadMethod == "html":
          directory = settings[1]["directories"]["html"]
        else:
          directory = settings[1]["directories"]["ftp"]
        
      except:
          print "error: could not get settings"
          sys.exit(1)   
          
  except:
    print "error: settings file not found: " + settings_file
    sys.exit(1)
    

  main(downloadMethod, ip, username, password, directory, fileName)
  
