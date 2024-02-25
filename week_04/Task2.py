# stats_and_max_values.py

import pandas as pd

# Reading the CSV file
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\week_04\menu.csv"
data = pd.read_csv(file_path)

# Checking statistical facts for all columns
statistical_facts = data.describe()
print(statistical_facts)

# Calculating the maximum value of specified attributes
attributes = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 
              'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 
              'Calcium (% Daily Value)', 'Iron (% Daily Value)']

max_values = data[attributes].max()
print("\nMaximum values for specified attributes:")
print(max_values)
