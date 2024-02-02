#How to compute the determinant of an array using NumPy?

import numpy as np

matrix = np.random.rand(3, 3)
determinant = np.linalg.det(matrix)
print(determinant)