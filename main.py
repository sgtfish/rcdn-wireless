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

#FTP - Requires no directory input = ""
#HTML - Requires '/' for directory
#SSH - Requires full pwd for directory

def main():
  downloadMethod = "ssh"
  ip = "10.154.66.159"
  directory = "/home/pi/sftp/"
  username = "pi"
  password = "raspberry"
  fileName = "actions.json"

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
  """
  ---------------------------------
  Method 1: using argparse module
  ---------------------------------
  parser = argparse.ArgumentParser()
  parser.add_argument("downloadMethod", help="The download method to use (ssh, ftp, or http)")
  parser.add_argument("ip", help="The ip address of the server")
  parser.add_argument("username", help="Username for logging in")
  parser.add_argument("password", help="Password of username")
  parser.add_argument("directory", help="The directory where the file is located on the server")
  parser.add_argument("fileName", help="Name of file to be used for parsing")
  args = parser.parse_args()
    
  downloadMethod = args.downloadMethod
  ip = args.ip
  username = args.username
  password = args.password
  directory = args.directory
  fileName = args.fileName
  
  ---------------------------------
  Method 2: using sys.argv
  ---------------------------------
  if sys.argv[1] == "-h" and len(sys.argv) == 2:
    print "Help:\n"
    print "  downloadMetod    The download method to use (ssh, ftp, or http)"
    print "  ip               The ip address of the server"
    print "  username         Username for logging in"
    print "  password         Password of username"
    print "  directory        The directory where the file is located on the server"
    print "  fileName         Name of file to be used for parsing"
    sys.exit(1)
  if len(sys.argv[1:]) != 6:
    print "error: not enough arguments"
    print "usage: main.py [-h] downloadMethod ip username password directory fileName"
    sys.exit(1) 
   
  downloadMethod = sys.argv[1]
  ip = sys.argv[2]
  username = sys.argv[3]
  password = sys.argv[4]
  directory = sys.argv[5]
  fileName = sys.argv[6]  
  """
  main(downloadMethod, ip, username, password, directory, fileName)
  
