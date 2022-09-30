import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

x = np.array([-3, -2, 0, 3])
y = np.array([9, 10, -6, 15])

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


# Interpolate graph by adding intermediate values
x_interp = np.linspace(np.min(x), np.max(x), 100)
y_interp = [calculate(x, y, i) for i in x_interp]

plt.style.use('cyberpunk')
plt.grid(True)
plt.title('Графік Лангранжа')

# Show graph
plt.plot(x, y, 'o', x_interp, y_interp)
plt.show()
