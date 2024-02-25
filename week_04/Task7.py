# horizontal_bar_graph.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the CSV file
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\week_04\menu.csv"
data = pd.read_csv(file_path)

# Defining a list of unique categories
categories = data['Category'].unique()

# Looping through each category and drawing a horizontal bar plot for items against calories
for category in categories:
    plt.figure(figsize=(20, 15))
    category_df = data[data['Category'] == category]
    sns.barplot(x='Calories', y='Item', data=category_df, color='red')
    plt.title(f'Calories in Items - {category}')
    plt.xlabel('Calories', fontweight='bold')
    plt.ylabel('Item', fontweight='bold')
    plt.show()
