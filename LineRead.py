#!/usr/bin/python

import RobotGPIO
import sqlite3
import pdb

# Return the concatonated values of the sensor inputs (number of possible states == 2^(number_of_sensors)-1)
def sensorRead():
  L = RobotGPIO.leftSensor()
  R = RobotGPIO.rightSensor()
  return str(L)+str(R)

def main():
  conn = sqlite3.connect('line.db')
  c = conn.cursor()
  #c.execute("CREATE TABLE line (error STRING, error_previous STRING, id INTEGER)")        # this line and the following commented out as it is only necessary when initializing the DB
  #c.execute("INSERT INTO line (error, error_previous, id) VALUES (3.1415, 666, 1)")
  while(1):
    current_error = sensorRead()
    c.execute("UPDATE line set error ="+current_error+" WHERE id = 1;")
    previous_error = current_error
    c.execute("UPDATE line SET error_previous ="+previous_error+" WHERE id = 1;") 
    conn.commit()



if __name__ == '__main__':
  main()
