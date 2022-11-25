import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + math.sin(y / math.sqrt(11))

x0 = 0.6
b = 1.6
h = 0.1

x = np.arange(x0, b + h, h)
n = len(x) - 1
y = np.empty(n + 1)

y[0] = 1.2

for i in range(n):
    y[i + 1] = y[i] + f(x[i], y[i]) * h

y_rounded = np.round_(y, 4)

print('x =', x)
print('y =', y_rounded)

plt.plot(x, y, 'o', x, y, 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Ейлера')
plt.legend(['точки', 'x + math.sin(y / math.sqrt(11))'])
plt.grid()
plt.show()
