#!/usr/bin/python


import os
import glob
import pdb
import sqlite3

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

def read_temp():
  lines = read_temp_raw()
  while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = read_temp_raw()
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string) / 1000.0
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c

def read_temp_env():
  return os.getenv("PYTEMP")

def main():
  conn = sqlite3.connect('temp.db')
  c = conn.cursor()
  #c.execute("CREATE TABLE temps (temp REAL, id INTEGER)")        # this line and the following commented out as it is only necessary when initializing the DB
  #c.execute("INSERT INTO temps (temp, id) VALUES (3.1415, 1)")
  while(1):
    #pdb.set_trace()
    c.execute("UPDATE temps SET temp ="+str(read_temp())+" WHERE id = 1;")
    conn.commit()
    #os.environ["PYTEMP"] = str(read_temp())
    
if __name__ == '__main__':
  main()
