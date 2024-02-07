import pandas as pd

#defining the data dictionary with the data given
data = {
    'Name': ['Sonia', 'Bilal', 'Hifza', 'Kabir', 'Jazim'],
    'Age': [27, 24, 22, 32, 23],
    'Address': ['Lahore', 'Karachi', 'Sialkot', 'Peshawar', 'Ihr'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd', 'Bsc']
}
# Creating DataFrame named: AICP_DF
AICP_DF = pd.DataFrame(data)

# Selecting 'Name' and 'Qualification' columns and save to df1(dataframe 1)
df1 = AICP_DF[['Name', 'Qualification']]

# Adding a new column "Height" to AICP_DF
AICP_DF['Height'] = [5.1, 6.2, 5.1, 5.2, 5.1]

# Setting up column "Name" as the index column
AICP_DF.set_index('Name', inplace=True)

# Retrieving the row with index "Hifza"
row_hifza = AICP_DF.loc['Hifza']

# Retrieving the row with index 3
row_index_3 = AICP_DF.iloc[3]

# Dropping the row with index "Bilal"
AICP_DF.drop(index='Bilal', inplace=True)

# Displaying the resulting DataFrame AICP_DF and all other performed operations
print("AICP_DF:")
print()
print(AICP_DF)

print("\ndf1:")
print(df1)

print("\nRow with index 'Hifza':")
print(row_hifza)

print("\nRow with index 3:")
print(row_index_3)
