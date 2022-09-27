from scipy.misc import derivative

def f(x):
    return 4 * pow(x, 4) + 4 * pow(x, 3) - 6 * pow(x, 2) - 9 * x - 1

a = -2
b = -.5
eps = 0.001

if derivative(f, a) * derivative(f, a, 2) < 0:
    a, b = b, a

xp1 = a
xp2 = b

while True:
    xn1 = xp1 - f(xp1) * (xp2 - xp1) / (f(xp2) - f(xp1))
    xn2 = xp2 - f(xp2) - derivative(f, xp2)

    xp1 = xn1
    xp2 = xn2

    if xp2 - xp1 >= eps:
        break

x = (xp1 + xp2) / 2

print(x)
