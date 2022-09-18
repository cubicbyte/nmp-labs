# Піднести матриці до степеня

import numpy as np

matrix = np.matrix(
    [[-1, 0, 2],
    [0, 1, 0],
    [1, 2, -1]]
)

mx_power = np.linalg.matrix_power(matrix, 2)

print(mx_power)
