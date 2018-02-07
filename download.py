import paramiko, os, urllib
import syslogger
from ftplib import FTP
import pdb
import sys

local_dir = '/home/pi/rcdn-wireless/'

FACILITY = "download.py"

def ssh(ip, filepath, userid, password, filename):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  try:
    syslogger.log(FACILITY,"INFO","Starting SSH connection")
    ssh.connect(ip, 22, userid, password)
    sftp = ssh.open_sftp()
    syslogger.log(FACILITY,"INFO","Connected to IP via SSH")
  
    syslogger.log(FACILITY,"INFO","Attempting to download file")
    sftp.get(filepath + filename, local_dir + filename)
    syslogger.log(FACILITY,"INFO","Successfully downloaded file")
    sftp.close()
    ssh.close()
    syslogger.log(FACILITY,"INFO","Closed SSH connection")
  except:
    syslogger.log(FACILITY,"ERROR","Failed to connect or download file")
    sys.exit(1)

def ftp(ip, filepath, userid, password, filename):
  syslogger.log(FACILITY,"INFO","Connecting to FTP server")
  try:
    ftp = FTP(ip)
    ftp.login(userid, password)
    file = open(filename, 'wb')

    syslogger.log(FACILITY,"INFO","Attempt to download file")
    ftp.retrbinary('RETR ' + filepath + filename, file.write, 1024)
    syslogger.log(FACILITY,"INFO","Successfully downloaded file")

    ftp.quit()
    file.close()
    syslogger.log(FACILITY,"INFO","Closed FTP connection")
  except:
    syslogger.log(FACILITY,"ERROR","Failed to connect or download file")
    sys.exit(1)

def html(ip, filepath, userid, password, filename):
  syslogger.log(FACILITY,"INFO","Connecting to HTML server") # HTTP server?
  try:
    url = "http://" + ip + filepath + filename
    syslogger.log(FACILITY,"INFO","Downloading file")
    response = urllib.urlopen(url).read()

    f = open(filename, 'w')
    f.write(response)
    syslogger.log(FACILITY,"INFO","Successfully downloaded file")
    f.close
    syslogger.log(FACILITY,"INFO","Closed HTML connection") # HTTP connection?
  except:
    syslogger.log(FACILITY,"ERROR","Failed to connect or download file")
    sys.exit(1)

def downloadFile(downloadMethod, ip, directory, username, password, fileName):
  if(downloadMethod == "ssh"):
    ssh(ip,directory,username,password,fileName)
  elif(downloadMethod == "ftp"):
    ftp(ip,directory,username,password,fileName)
  elif(downloadMethod == "html"):
    html(ip,directory,username,password,fileName)
  else:
    syslogger.log("Main","ERROR","Invalid download method")
    sys.exit(1)
