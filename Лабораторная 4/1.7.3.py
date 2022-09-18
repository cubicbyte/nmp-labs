# Визначити ранг матриці

import numpy as np

matrix = np.matrix([[-2, 3, 1, -1], [3, 2, 1, 4], [1, 2, 3, 4], [0, 2, 3, 3]])
res = np.linalg.matrix_rank(matrix)

print(res)
