# Створіть прямокутну матрицю A з N рядками та стовпцями M з випадкових елементів.
# Знайдіть найнижче значення серед середніх значень для кожного рядка матриці.

import numpy as np

N = 3
M = 4

a = np.random.randint(0, 10, (N, M))

avg = a.mean(1)
min_avg = min(avg)

print('matrix\n', a.view())
print('avg rows\n', avg.view())
print('min avg\n', min_avg)
