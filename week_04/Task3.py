# correlation_matrix.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV file
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\week_04\menu.csv"
data = pd.read_csv(file_path)

# Dropping non-numeric columns
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Calculating correlation matrix
correlation_matrix = numeric_data.corr()

# Plotting the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm',  fmt=".2f", linewidths=1.0)
plt.title('Correlation Matrix')
plt.show()
