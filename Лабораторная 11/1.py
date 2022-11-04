import numpy as np
import matplotlib.pyplot as plt

def formula(x):
    return np.cos(3 * x) - 3 * x + 3



x = np.array([i * 0.1 for i in range(1, 11)])
y = np.array([formula(x)])

x_avg  = np.mean(x)
y_avg  = np.mean(y)
x2_avg = np.mean(x ** 2)
xy_avg = np.mean(x * y)

a = (xy_avg - x_avg * y_avg) / (x2_avg * x_avg ** 2)
b = y_avg - (a * x_avg)



print('Коефіцієнти')
print('a = ', round(a, 2))
print('b = ', round(b, 2))

# Відобразити графік
plt.plot(x, a*x + b, 'r', label='Лінія')
plt.scatter(x, y,  label='Точкова діаграма')

plt.title('Результат')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
