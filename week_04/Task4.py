# boxplot.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV file
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\week_04\menu.csv"
data = pd.read_csv(file_path)

# Plotting the boxplot
plt.figure(figsize=(15, 10))
sns.boxplot(x='Calories', y='Category', data=data)
plt.title('Boxplot')
plt.show()
