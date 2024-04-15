from flask import Flask, render_template
import csv
import pandas as pd

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the data page
@app.route('/data')
def data():
    data = []

    # Read data from CSV file
    with open('onlinefood.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    
    return render_template('data.html', data=data)


# Function to get column names and data types from the CSV file
def get_column_info(csv_file):
    # Read the first row of the CSV file to get column names
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        column_names = next(reader)
    
    # Read the CSV file using Pandas to infer data types
    df = pd.read_csv(csv_file)
    data_types = df.dtypes.tolist()
    
    # Zip column names and data types together
    column_info = list(zip(column_names, data_types))
    
    return column_info

# Route for the about page
@app.route('/about')
def about():
    # Get column information from the CSV file
    column_info = get_column_info('onlinefood.csv')
    
    return render_template('about.html', column_info=column_info)

if __name__ == '__main__':
    app.run(debug=True)


