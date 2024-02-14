import matplotlib.pyplot as plt

# Data of programming languages and their popularity
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Creating a horizontal bar chart
plt.barh(languages, popularity, color='Green', alpha=0.8)

# Adding labels and title
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages : AICP Internship week-3 Task-4')

# Adding a grid to both axes
plt.grid(True, axis='both', linestyle='-', alpha=0.7,)



# Showing the plot
plt.show()
