#This program allows to retrieve the data sent by the sensor and record it in a csv file

# Import to read what the microcontroller sends
import serial
import time
import datetime

# Import for recording
import pandas as pd
import numpy as np

# Import for user information (only the name + first name will be used)
import info_user as iu



ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) # check that 'COM#' is the one that appears in the device manager
time.sleep(2)

name=iu.name + "_" + iu.fname

values = []
time=[]
arr = np.array(["",[],[]])

for i in range(iu.record):
    line = ser.readline()                   # read a byte string
    if line:    
        string = line.decode()              # convert the byte string to a unicode string
        num = int(string)                   # convert the unicode string to an int
        print(num)
        values.append(num)                  # adds the read value to the values list
        time.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))      # adds the time to the time list
ser.close()

# Transform the lists into a numpy array
arr[0] = name
arr[1] = time
arr[2] = values

arr = np.array(arr) 

# Transform the array into a dataframe (understandable by pandas)
df = pd.DataFrame(arr) 

# Save the dataframe in a csv file in the "dataframes" folder (which is used to store all data)
path = 'dataframes/'
name= arr[0]+ "_" +time[0] +'.csv'
df.to_csv(path+name)