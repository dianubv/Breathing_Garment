import serial
import time
import datetime

import pandas as pd
import numpy as np



# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)

print('Enter your name: ')
name=input()

data = []
time=[]
table=[]
for i in range(70):
    line = ser.readline()   # read a byte string
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int
        print(num)
        data.append(num) # add int to data list
        time.append(datetime.datetime.now())
ser.close()
table[0]=name
table[1]=time
table[2]=data

arr = np.array(table) #pour que db comprenne table

# transforme le tableau en dataframe (comprehensible par pandas)
df = pd.DataFrame(arr)


# là on a table qui est un tableau de 2 tableaux, le premier contient le nom, le second le temps, le troisième les données

# build the plot
""" plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Stretch sensor resistance')
plt.title('Stretch sensor resistance by time')
plt.show() """