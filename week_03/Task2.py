import matplotlib.pyplot as plt

# Defining coordinates for the both the lines
x = [10, 20, 30]
y1 = [20, 40, 10]
y2 = [40, 10, 30]

# Plotting the lines with specific color and width
line1, = plt.plot(x, y1, label='Line 1', color='blue', linewidth=3)
line2, = plt.plot(x, y2, label='Line 2', color='red', linewidth=5,)

# Getting line widths dynamically 
line1_width = line1.get_linewidth()
line2_width = line2.get_linewidth()

# Adding legend with dynamic width
plt.legend([f'Line 1-width-{line1_width}', f'Line 2-width-{line2_width}'])


# Adding labels and title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('AICP Internship week-3 Task-2')

# Setting the axis limits
plt.xlim(10, 30)
plt.ylim(10, 40)

# Setting displaying ticks on x-axis
plt.xticks([10, 15, 20, 25, 30])

# dsiplaying the plot
plt.show()
