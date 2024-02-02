#How to compute the cross-product of two matrices in NumPy?


import numpy as np

matrix1 = np.random.rand(3, 3)
matrix2 = np.random.rand(3, 3)

cross_product = np.cross(matrix1, matrix2)
print(cross_product)