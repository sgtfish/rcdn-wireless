#!/usr/bin/python
import time
import robotInverse
import robotGPIO
import os
import pdb
import download
import parse

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
  
  if(downloadMethod == "ssh"):
    print "Entering ssh download"
    download.ssh(ip,directory,username,password,fileName)
  elif(downloadMethod == "ftp"):
    print "Entering ftp download"
    download.ftp(ip,directory,username,password,fileName)
  elif(downloadMethod == "html"):
    print "Entering html download"
    download.html(ip,directory,username,password,fileName)
  else:
    

  parse.parseFile(fileName)

if __name__ == '__main__':
  main()
