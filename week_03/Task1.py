import matplotlib.pyplot as plt

# Defining the x and y coordinates
x = [1.0, 2.0, 3.0]
y = [2.0, 4.0, 1.0]

# Creating the plot
plt.plot(x, y)

# Adding the basic labels and title
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Basic line graph : AICP Internship week-3 Task-1")

# Setting the axis limits
plt.xlim(1, 3)
plt.ylim(1, 4)

# Setting displaying ticks on x-axis
plt.xticks([1, 1.5, 2, 2.5, 3])

# Displaying the plot
plt.show()
