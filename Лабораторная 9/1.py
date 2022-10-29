import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate

x = [0.3,  0.5,  0.8,  1.2,  1.8 ]
y = [1.19, 2.65, 1.83, 3.84, 2.86]

spl = scipy.interpolate.UnivariateSpline(x, y)
xs = np.linspace(x[0], x[4], 100)

plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.show()
