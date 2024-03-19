#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd

# Loading the CSV file
file_path = r"C:\Users\Arsal Naveed\Desktop\AICP Internship\week_06\births.csv"
df = pd.read_csv(file_path)

# Extracting the decade from the 'year' column and creating a new column 'Decade'
df['Decade'] = (df['year'] // 10) * 10

# Displaying the first few rows of the DataFrame with the new 'Decade' column
print(df.head())

# Saving the modified DataFrame
df.to_csv(file_path, index=False)


# In[29]:


df.describe()


# In[30]:


# Checking for missing values in the DataFrame
missing_values = df.isnull().sum()

# Displaying the count of missing values for each column
print("Missing values per column:")
print(missing_values)


# In[31]:


import matplotlib.pyplot as plt

# Grouping the data by decade and gender and calculating the sum of births
births_by_decade_gender = df.groupby(['Decade', 'gender'])['births'].sum().unstack()

# Plotting the trend of male and female births every decade
births_by_decade_gender.plot(kind='bar', figsize=(10, 6))
plt.title('Trend of Male and Female Births Every Decade')
plt.xlabel('Decade')
plt.ylabel('Number of Births')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[32]:


import numpy as np

# Calculating the mean and standard deviation of the 'births' column
mean_births = df['births'].mean()
std_births = df['births'].std()

# Defining the lower and upper bounds for filtering outliers
lower_bound = mean_births - 5 * std_births
upper_bound = mean_births + 5 * std_births

# Filtering the DataFrame to include only rows where 'births' fall within the specified bounds
filtered_df = df[(df['births'] >= lower_bound) & (df['births'] <= upper_bound)]

# Displaying the shape of the filtered DataFrame to compare with the original DataFrame
print("Original DataFrame shape:", df.shape)
print("Filtered DataFrame shape:", filtered_df.shape)


# In[33]:


# Creating a figure and axis for the box plot
plt.figure(figsize=(10, 6))

# Ploting box plot before filtering outliers
plt.subplot(1, 2, 1)
plt.boxplot(df['births'], vert=False)
plt.title('Box Plot of Births (Before Filtering)')
plt.xlabel('Number of Births')

# Ploting box plot after filtering outliers
plt.subplot(1, 2, 2)
plt.boxplot(filtered_df['births'], vert=False)
plt.title('Box Plot of Births (After Filtering)')
plt.xlabel('Number of Births')

plt.tight_layout()
plt.show()


# In[34]:


# Plotting births by weekday for several decades using a bar graph
births_by_weekday_decade.plot(kind='bar', figsize=(12, 6))
plt.title('Births by Weekday for 1960,70,80 ')
plt.xlabel('Decade')
plt.ylabel('Number of Births')
plt.xticks(range(len(births_by_weekday_decade.index)), [str(year) + 's' for year in births_by_weekday_decade.index], rotation=45)
plt.legend(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], loc='upper right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[35]:


# Grouping the data by month and calculating the sum of births for each month
births_by_month = df.groupby('month')['births'].sum()

# Grouping the data by day and calculating the sum of births for each day
births_by_day = df.groupby('day')['births'].sum()

# Displaying the result
print("Births by Month:")
print(births_by_month)

print("\nBirths by Day:")
print(births_by_day)


# In[36]:


# Combining month and day into a single column to create a date without the year
df['date'] = df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# Grouping the data by date and calculating the average number of births for each date
average_births_by_date = df.groupby('date')['births'].mean()

# Plotting the time series of average number of births by date
plt.figure(figsize=(12, 6))
average_births_by_date.plot()
plt.title('Average Number of Births by Date of the Year')
plt.xlabel('Date')
plt.ylabel('Average Number of Births')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




