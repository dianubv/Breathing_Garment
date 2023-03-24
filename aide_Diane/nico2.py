import pandas as pd
import numpy as np
import sqlite3

# create a numpy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# create a pandas dataframe from the numpy array
df = pd.DataFrame(arr)

# create a connection to the database
conn = sqlite3.connect('example.db')

# write the dataframe to a SQL table
df.to_sql('example_table', conn, if_exists='replace')