# Знайти обернену матрицю до матриць

import numpy as np

matrix = np.matrix(
    [[1, 1, 1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1]]
)

res = np.linalg.inv(matrix)

print(res)
