import sympy as sp
from math import factorial

def calc(x):
    d1 = sp.diff(f, x)
    d2 = sp.diff(d1, x)
    d3 = sp.diff(d2, x)
    y = f + d1 * x + d2 * (x-0) ** 2 / factorial(2) + d3 * (x-0) ** 3 / factorial(3)

    return y

x = sp.symbols('x')
f = sp.cos(3*x) - 3*x + 3

sp.plot(calc(x), f, (x, -1, 1), label='Результат')
