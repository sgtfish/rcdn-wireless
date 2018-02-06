#!/usr/bin/python
#
import time
import robotInverse
import robotGPIO
import os
import pdb
import download
import parse


def main():
  downloadMethod = "SSH"
  ip = "192.168.1.20"
  directory = "FTP/"
  username = "pi"
  password = "raspberry"
  fileName = "test.json"
  
  if(downloadMethod == "ssh"):
    download.ssh(ip,directory,username,password,fileName)
  elif(downloadMethod == "telnet"):
    download.telnet(ip,directory,username,password,fileName)
  elif(downloadMethod == "html"):
    download.html(ip,directory,username,password,fileName)
  else:
    "failed"


if __name__ == '__main__':
  main()
