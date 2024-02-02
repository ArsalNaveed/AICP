#How to create a 5x5 array with random values and find the minimum and maximum values using
#NumPy?

import numpy as np

random_5x5_array = np.random.rand(5, 5)
min_value = np.min(random_5x5_array)
max_value = np.max(random_5x5_array)
print("Min Value:", min_value)
print("Max Value:", max_value)
