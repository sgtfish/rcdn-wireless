import paramiko, os, urllib
from ftplib import FTP

def ssh(ip, filepath, userid, password, filename):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  
  #Start Connections
  ssh.connect(ip, 22, userid, password)
  sftp = ssh.open_sftp()

  #Pull file
  sftp.get(filepath + filename, '/home/pi/Piathlon/' + filename)

  #Close connections
  sftp.close()
  ssh.close()

def ftp(ip, filepath, userid, password, filename):
  ftp =FTP (ip)
  ftp.login(userid, password)
  file = open(filename, 'wb')

  ftp.retrbinary('RETR ' + filepath + filename, file.write, 1024)

  ftp.quit()
  file.close()

def html(ip, filepath, userid, password, filename):
  url = "http://" + ip + filepath 

  response = urllib.urlopen(url).read()

  f = open(filename, 'w')
  f.write(response) 
  f.close 
