from scipy import integrate
from math import tan

eps = 0.001

def formula(x):
    return tan(x ** 2) / (x + 1)

def left(formula, a, b, n):
    h = (b - a) / n
    sum = 0

    for i in range(0, n):
        sum += formula(a + i * h)

    return sum * h



v,err = integrate.quad(formula, 1.2, 2)

if abs(left(formula, 1.2, 2, 2 * 10) - left(formula, 1.2, 2, 10)) / 3 <= eps:
    print('Лівий прямокутник:', round(left(formula, 1.2, 2, 10), 5))



def right(formula,a,b,n):
    h = (b - a) / n
    sum = 0

    for i in range(1, n + 1):
        sum += formula(a + i * h)

    return sum * h

print('Правий прямокутник:', round(right(formula, 1.2, 2, 10), 5))



def avg(formula, a, b, n):
    h = 0.08
    sum = 0

    for i in range(0, n):
        sum += formula(a + i * h)

    return sum * h

print('Середній прямокутник:', round(avg(formula,1.2,2,10), 5))
print('Перевірка:', round(v, 5))
