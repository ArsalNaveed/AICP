#How to compute the mean, standard deviation, and variance of a given array along the second axis in
#NumPy?

import numpy as np

given_array = np.random.rand(4, 5)
mean_value = np.mean(given_array, axis=1)
std_deviation = np.std(given_array, axis=1)
variance = np.var(given_array, axis=1)

print("Mean along the second axis is:", mean_value)
print("Standard Deviation along the second axis is:", std_deviation)
print("Variance along the second axis is:", variance)
