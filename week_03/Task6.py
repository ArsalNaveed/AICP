import pandas as pd
import matplotlib.pyplot as plt

# Reading the excel file
file_path = "C:\\Users\\Arsal Naveed\\Desktop\\AICP Internship\\week_03\\goldmedals.xlsx"
data = pd.read_excel(file_path)

# Selecting the required columns
countries = data['Country']
gold_medals = data['Gold Medals']

# Finding the index of the country with the most Gold Medals
max_index = gold_medals.idxmax()

# Creating explode values to pop out the country with the most Gold Medals
explode = [0.1 if i == max_index else 0 for i in range(len(countries))]

# Creating a pie chart with the country of the most Gold Medals popped out
plt.figure(figsize=(8, 8))
plt.pie(gold_medals, labels=countries, autopct='%1.1f%%', startangle=140, explode=explode, wedgeprops={'linewidth': 1, 'edgecolor': 'black'})
plt.title('Gold Medal Achievements : AICP Internship week-3 Task-6')
plt.axis('equal')  

# Showing the plot
plt.show()
