# stripplot.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV file
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\week_04\menu.csv"
data = pd.read_csv(file_path)

# Defining the list of attributes
attributes = ['Calories', 'Total Fat', 'Carbohydrates', 'Dietary Fiber', 'Sugars', 
              'Protein', 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)', 
              'Calcium (% Daily Value)', 'Iron (% Daily Value)']

# Looping through each attribute and drawing a stripplot
for attribute in attributes:
    plt.figure(figsize=(14, 8))
    sns.stripplot(x='Category', y=attribute, data=data, jitter=True)
    plt.title(f'Stripplot of {attribute} by Category')
    plt.xlabel('Category')
    plt.ylabel(attribute)
    plt.show()
