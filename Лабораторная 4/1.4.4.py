# Обчислити визначники

import numpy as np

matrix = np.matrix([[1, 2, 3], [-1, 2, 1], [1, 3, 2]])
res = np.linalg.det(matrix)

print(res)
