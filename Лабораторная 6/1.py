import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk
from scipy.interpolate import lagrange

x_arr = np.array([-3, -2, 0, 3])
y_arr = np.array([9, 10, -6, 15])

def calculate(x, y, t):
    res = 0

    for j in range(len(y)):
        p1 = 1
        p2 = 1

        for i in range(len(x)):
            if i != j:
                p1 *= t - x[i]
                p2 *= x[j] - x[i]

        res += y[j] * p1 / p2

    return res

# Calculate values
for x in x_arr:
    print('x={x}; y={y}'.format(x=x, y=calculate(x_arr, y_arr, x)))

# Interpolate graph by adding intermediate values
x_interp = np.linspace(np.min(x_arr), np.max(x_arr), 100)
y_interp = [calculate(x_arr, y_arr, x) for x in x_interp]

plt.style.use('cyberpunk')
plt.grid(True)
plt.title('Графік Лангранжа')

# Show graph
plt.plot(x_arr, y_arr, 'o', x_interp, y_interp)
plt.show()



# Test
f = lagrange(x_arr, y_arr)
fig = plt.figure(figsize = (10, 8))
plt.plot(x_interp, f(x_interp), 'b', x_arr, y_arr, 'ro')
plt.title('Тест')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
