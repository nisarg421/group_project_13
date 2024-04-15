import sqlite3
import pandas as pd

# Connect to SQLite database (creates if doesn't exist)
conn = sqlite3.connect('survey_data.db')

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Create survey_data table
cur.execute('''CREATE TABLE IF NOT EXISTS survey_data (
               age INTEGER,
               gender TEXT,
               marital_status TEXT,
               occupation TEXT,
               monthly_income TEXT,
               educational_qualifications TEXT,
               family_size INTEGER,
               latitude REAL,
               longitude REAL,
               pin_code INTEGER,
               output TEXT,
               feedback TEXT
               )''')

# Read dataset from CSV file
df = pd.read_csv('onlinefood.csv')  # Replace 'dataset.csv' with the filename of your dataset

# Replace spaces with underscores in column names
df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)

# Insert data into the survey_data table
df.to_sql('survey_data', conn, if_exists='append', index=False)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and table created successfully.")

