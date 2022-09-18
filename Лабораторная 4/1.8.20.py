# Розв’язати систему лінійних рівнянь методом Крамера, матричним методом

import numpy as np

a = np.matrix([[2, -1 ,1], [3, 4, -2], [1, -3, 1]])
b = np.matrix([[5], [-3], [4]])

res = np.linalg.solve(a, b)

print(res)
