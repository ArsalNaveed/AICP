import matplotlib.pyplot as plt

# defining coordinates for the both the lines
x = [1.0, 4.0, 5.0, 6.0, 7.0]
y = [2.0, 6.0, 3.0, 6.0, 3.0]
y1= [4.0, 8.0, 5.0, 8.0, 5.0]

# Plotting the lines with style, color and label
plt.plot(x, y, linestyle='dotted',color= 'red', label='Line with blue circle marker')
plt.plot(x, y1, color='green' ,label='Line with red square marker')

# Defining the marker with its shape and color
plt.scatter(x, y, marker='o', color='blue')
plt.scatter(x, y1, marker='s', color='red')

# Adding a legend
plt.legend()

# Adding labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('AICP Internship week-3 Task-3')

# Setting the axis limits
plt.xlim(1, 8)
plt.ylim(1, 9)

# Showing the plot
plt.show()
