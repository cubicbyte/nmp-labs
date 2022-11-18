from scipy import integrate
from math import sqrt

eps = 0.001

def formula(x):
    return 1 / sqrt(x ** 2 - 1)

def calculate(a,b,n):
    h = (b - a) / n
    integr = formula(a) + formula(b)

    for i in range(1,n):
        k = a + i * h

        if i % 2 == 0:
            integr += 2 * formula(k)
        else:
            integr += 4 * formula(k)

    integr *= h / 3
    return integr

if abs(calculate(1.6, 2.4, 2 * 8) - calculate(1.6, 2.4, 8)) / 15 <= eps:
    print('Метод Сімпсона:', round(calculate(1.6, 2.4, 8), 5))

v = integrate.quad(formula, 1.6, 2.4)[0]
print('Перевірка методу:', round(v, 5))
