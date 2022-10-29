import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x = [0.3,  0.5,  0.8,  1.2,  1.8 ]
y = [1.19, 2.65, 1.83, 3.84, 2.86]

spl = UnivariateSpline(x, y)
xs = np.linspace(x[0], x[4], 100)

plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.show()
