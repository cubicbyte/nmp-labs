import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + math.sin(y / math.sqrt(0.7))

x0 = 1.2
b = 2.2
h = 0.1

x = np.arange(x0, b + h, h)
n = len(x) - 1
y = np.empty(n + 1)

y[0] = 1.4

for i in range(n):
    y[i + 1] = y[i] + (f(x[i], y[i]) + f(x[i + 1], y[i] + h * f(x[i], y[i]))) * h / 2

y_rounded = np.round_(y, 4)

print('x =', x)
print('y =', y_rounded)

plt.plot(x, y, 'o', x, y, 'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Ейлера-Коші')
plt.legend(['Точки', 'x + math.sin(y / math.sqrt(0.7))'])
plt.grid()
plt.show()
