# This program allows to retrieve user information and store them in the breathing database

import mysql.connector

# Create a connection to the breathing database
conn = mysql.connector.connect(user='root', password='brg',
                               host='localhost',
                               database='breathing')

# Create the cursor that will execute queries
cursor = conn.cursor()

# Create the users table if it does not exist
cursor.execute(f'CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL AUTO_INCREMENT, first_name VARCHAR(30) NOT NULL, name VARCHAR(30) NOT NULL, birth_date DATE NOT NULL, PRIMARY KEY (id))')

# Ask user for information
fname =input('Enter your first name: ')
name =input('Enter your name: ')
b_date =input('Enter your birthdate (YYYY-MM-DD): ')
record =input('Enter the record time: ')

# Add user information to the users table
query = "INSERT INTO users (name, first_name, birth_date) VALUES (%s, %s, %s)"
values = (name, fname, b_date)
cursor.execute(query, values)

conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()

