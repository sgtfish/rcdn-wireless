#!/usr/bin/python

import time
import robotInverse
import robotGPIO
import os
import pdb
import download
import parse


def main():
  downloadMethod = "telnet"
  ip = "192.168.1.20"
  directory = "FTP/"
  username = "pi"
  password = "raspberry"
  fileName = "test.json"
  
  if(downloadMethod == "ssh"):
    print "Entering ssh download"
    download.ssh(ip,directory,username,password,fileName)
  elif(downloadMethod == "telnet"):
    print "Entering telnet download"
    download.telnet(ip,directory,username,password,fileName)
  elif(downloadMethod == "html"):
    print "Entering html download"
    download.html(ip,directory,username,password,fileName)
  else:
    "failed"


if __name__ == '__main__':
  main()
