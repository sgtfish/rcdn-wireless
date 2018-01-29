import paramiko, os, urllib, 
import syslogger
from ftplib import FTP

local_dir = '/home/pi/Piathlon/'


def ssh(ip, filepath, userid, password, filename):  
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
  try:
    syslogger.log("Downloader","INFO","Starting SSH connection")
    ssh.connect(ip, 22, userid, password)
    sftp = ssh.open_sftp()

    syslogger.log("Downloader","INFO","Downloading file.")
    sftp.get(filepath + filename, local_dir + filename)
    syslogger.log("Downloader","INFO","Successfully downloaded file")
    sftp.close()
    ssh.close()
    syslogger.log("Downloader","INFO","Closed SSH connection")
  except:
    syslogger.log("Downloader","ERROR","Failed to connect or download file")

def ftp(ip, filepath, userid, password, filename):
  syslogger.log("Downloader","INFO","Connecting to FTP server")
  try:
    ftp =FTP (ip)
    ftp.login(userid, password)
    file = open(filename, 'wb')

    syslogger.log("Downloader","INFO","Downloading file")
    ftp.retrbinary('RETR ' + filepath + filename, file.write, 1024)
    syslogger.log("Downloader","INFO","Successfully downloaded file")

    ftp.quit()
    file.close()
    syslogger.log("Downloader","INFO","Closed FTP connection")
  except:
    syslogger.log("Downloader","ERROR","Failed to connect or download file")

def html(ip, filepath, userid, password, filename):
  syslogger.log("Downloader","INFO","Connecting to HTML server")
  try:
    url = "http://" + ip + filepath + filename
    syslogger.log("Downloader","INFO","Downloading file")
    response = urllib.urlopen(url).read()

    f = open(filename, 'w')
    f.write(response) 
    syslogger.log("Downloader","INFO","Successfully downloaded file")
    f.close 
    syslogger.log("Downloader","INFO","Closed HTML connection")
  except:
    syslogger.log("Downloader","ERROR","Failed to connect or download file")
