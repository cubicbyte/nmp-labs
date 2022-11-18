from scipy import integrate
from math import sqrt

eps = 0.001

def formula(x):
    return 1 / sqrt(2 * x + 1.6)

def trapezoid(func, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        sum += func(a + i * h)

    return sum * h

def check() -> bool:
    return abs(trapezoid(formula, 3.2, 4, 2 * 10) - trapezoid(formula, 3.2, 4, 10)) / 3 <= eps



if check():
    print('Метод трапеції:', round(trapezoid(formula, 3.2, 4, 10), 5))

v = integrate.quad(formula, 3.2, 4)[0]
print('Перевірка методу трапеції', round(v, 5))
