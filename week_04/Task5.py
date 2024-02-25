# max_values_items.py

import pandas as pd

# Reading the CSV file
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\week_04\menu.csv"
data = pd.read_csv(file_path)

# Defining the columns to find the items with the highest quantity
columns_of_interest = [
    'Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars',
    'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)',
    'Calcium (% Daily Value)', 'Iron (% Daily Value)'
]

# Finding the item with the highest quantity for each of these columns
max_values_items = {column: data.loc[data[column].idxmax()] for column in columns_of_interest}

# Creating a summary dictionary to display the results
summary = {column: f"{max_values_items[column]['Item']} - {max_values_items[column][column]}" for column in columns_of_interest}
print(summary)
