from scipy import optimize
from math import sin, cos

x0 = 1.5
y0 = 0.5
delta = 0.1

def f1(y):
    return sin(y + 2) - 1.5

def f2(x):
    return -cos(x - 2) + 0.5

def f3(x):
    return 3 * x[0] + cos(x[0] + 0.5) - x[1] - 0.8, (sin(x[1])) / 2 - 0.8

def iter (x,y,e):
    xn = x
    yn = y

    xn1 = f2(x)
    yn1 = f1(y)

    n = 1

    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1

        xn1 = f2(yn)
        yn1 = f1(xn)

        n += 1

    print('x =', xn)
    print('y =', yn)

    print('Iterations:', n)

iter(x0, y0, 0.0001)

s = optimize.root(f3, [0, 0], method = 'hybr') 

print ('Check', s.x)
print ('Check', s.x)
