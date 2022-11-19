import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]


# 1)
time = np.linspace(0, 11, num=12)


# 2)
print(time)


# 3)
plt.plot(time, speed, '-o')
plt.grid()
plt.show()


# 4)
f = interp1d(time, speed, kind='cubic')
x = np.linspace(0, 11, num=10000)
y = f(x)

plt.plot(x, y, '-')
plt.show()
# 5)
v, err = quad(f, 0, 11)
print(v, err)


# 6)
f = interp1d(time, speed, kind='quadratic')
x = np.linspace(0, 11, num=10000)
y = f(x)

plt.plot(x, y, '-')
plt.show()
# 5)
v, err = quad(f, 0, 11)
print(v, err)

