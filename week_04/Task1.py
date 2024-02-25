# import_and_read.py

import numpy as np
import pandas as pd

# Reading the CSV file
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\week_04\menu.csv"
data = pd.read_csv(file_path)

# Displaying the first few rows of the dataset to ensure correct reading
print(data.head())
