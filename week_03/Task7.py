import matplotlib.pyplot as plt

# A sample data of math and science marks with the marks range
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Creating a scatter plot
plt.scatter(marks_range, math_marks, color='red', label='Mathematics')
plt.scatter(marks_range, science_marks, color='yellow', label='Science')

# Adding labels and title
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.title('Scatter Plot of Marks : AICP Internship week-3 Task-7')

# Adding a legend
plt.legend()

# Setting the axis limits
plt.xlim(0, 120)
plt.ylim(10, 110)
plt.yticks([20, 40, 60, 80, 100])

# Displaying the plot
plt.show()
