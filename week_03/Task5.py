import pandas as pd
import matplotlib.pyplot as plt

# Using a sample dataframe
data = {
    'a': [2, 4, 6, 8, 10],
    'b': [4, 2, 4, 2, 2],
    'c': [8, 5, 7, 4, 4],
    'd': [5, 7, 4, 8, 3],
    'e': [7, 6, 8, 6, 2]
}
# Creating the dataframe
df = pd.DataFrame(data)

# Plotting the DataFrame in a barchart with custom colors
df.plot(kind='bar', color = ['blue', 'green', 'red', 'purple', 'yellow'],alpha=0.8)
plt.title('Bar Plot using a DataFrame : AICP Internship week-3 Task-5')
plt.grid(True, axis='both', linestyle='--', alpha=0.7,)

# Setting the axis limits
plt.xlim(-0.5, 5)
plt.ylim(0, 10)

# Adding a legend
plt.legend()

# Showing the plot
plt.show()
