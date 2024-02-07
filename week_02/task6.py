import pandas as pd

# Defining the people.csv file path
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\EDA Internship 2.0 Week 2\people.csv"


# Defining the columns required to export
columns_to_import = ["First Name", "Sex", "Email", "Phone", "Job Title"]

# Defining the index columns
index_columns = ["Sex", "Job Title"]

# Defining the rows to skip
skip_rows = [1, 5]

# Importing the people.csv file
data = pd.read_csv(file_path, usecols=columns_to_import, skiprows=skip_rows)

# Seting index columns
data.set_index(index_columns, inplace=True)

# Exporting to the NewPeople.csv file
data.to_csv(r"C:\Users\Arsal Naveed\Desktop\AICP Internship\EDA Internship 2.0 Week 2\NewPeople.csv")
