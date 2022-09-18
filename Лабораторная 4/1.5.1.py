# Обчислити визначники

import numpy as np

matrix = np.matrix('''
    1  2  3  4;
    -2 1 -4  3;
    3 -4 -1  2;
    4  3 -2 -1
''')

res = np.linalg.det(matrix)

print(res)
