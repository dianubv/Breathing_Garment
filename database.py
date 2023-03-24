import mysql.connector
import hardware_to_db as hw

import pandas as pd
import numpy as np


# Creer la connection a la base de donnees breathing
conn = mysql.connector.connect(user='root', password='brg',
                               host='localhost',
                               database='breathing')

# dataframe
# write the dataframe to a MySQL table
name_table=  hw.table[0] + hw.table[2][0]   #à changer car on utilise array et numpy dans hardware_to_db
cursor = conn.cursor()
cursor.execute(f'CREATE TABLE IF NOT EXISTS {name_table} (name_user CHAR(20), time DATETIME, data FLOAT)')
df_tuple = [tuple(x) for x in hw.df.values]     # met data de table dans ce tuple
cursor.executemany(f'INSERT INTO {name_table} VALUES (%s, %s, %s)', df_tuple)
conn.commit()

# fermer le curseur et la connection
cursor.close()
conn.close()




##Ancenne version
""" mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="brg"
)

from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="brg",
    ) as connection:
        create_db_query = "CREATE TABLE " + hw.table[0] + hw.table[2][0] 
                #create a database with the name of the user and the date of the first measurement
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

#il manque de mettre toutes les données de table

print(mydb) 
 
# preparing a cursor object
cursorObject = mydb.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE ") """