# The program is a FastAPI that allows you to search for information on a "name" in both a database and CSV data.

import os
import mysql.connector
import pandas as pd

from fastapi import FastAPI

app = FastAPI()

# Make a connection to the database
conn = mysql.connector.connect(user='root', password='brg', host='localhost', database='breathing')

# request for testing
@app.get("/hw")
def rowot():
    return "hello world"

# request to search all information of "name" in the CSV file and in the database
@app.get("/{name}")
async def root(name: str):
    matching_files = find_name(name)                        # find all files that contain "name"
    results = {}
    for file_name in matching_files:                        # read all previous files and add them content in a dictionary
        file_path = os.path.join('dataframes', file_name)
        df = pd.read_csv(file_path)
        results[file_name] = df.to_dict(orient='records')   
    user_results = find_user(name)                          # find all users that contain "name" in the database
    return {"csv_files": results, "user_results": user_results}

# Function to find all files that contain "name" in the CSV files
def find_name(name: str):
    dir_path = 'dataframes'
    csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]
    matching_files = []
    for file_name in csv_files:                            # check if "name" is in the file name
        if name in file_name:
            matching_files.append(file_name)
    return matching_files                                  # return the list of files that contain "name"

# Function to find all users that contain "name" in the database
def find_user(name: str):
    cursor = conn.cursor()                                      # create a cursor to execute queries
    query = f"SELECT * FROM users WHERE name LIKE '%{name}%'"   # query to find all users that contain "name"
    cursor.execute(query)
    rows = cursor.fetchall()    
    user_results = []
    for row in rows:                                            # add the results in a list of dictionaries
        user_results.append({"id": row[0], "name": row[1], "first_name": row[2], "birth_date": row[3]})
    cursor.close()
    return user_results                                        # return the list of dictionaries of users "name"
