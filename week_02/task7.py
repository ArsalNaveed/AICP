import pandas as pd

# Defining the SampleWork.xlsx file path
file_path =  r"C:\Users\Arsal Naveed\Desktop\AICP Internship\EDA Internship 2.0 Week 2\SampleWork.xlsx"

# Importing data from sheet 1, skipping row 2, and setting row 2 as header
data = pd.read_excel(file_path, sheet_name=0, skiprows=[1], header=1)

# Selecting only the first and last columns
data = data.iloc[:, [0, -1]]

# Exporting to the NewSheet.xlsx file
data.to_excel(r"C:\Users\Arsal Naveed\Desktop\AICP Internship\EDA Internship 2.0 Week 2\NewSheet.xlsx", index=False)
