from scipy.misc import derivative

a = -2
b = -.5
eps = 0.001

def formula(x):
    return 4 * pow(x, 4) + 4 * pow(x, 3) - 6 * pow(x, 2) - 9 * x - 1



df2 = derivative(formula, b, n=2)

if (formula(b) * df2 > 0):
    x = b
else:
    x = a

df = derivative(formula, x, n=1)
result = x - formula(x) / df

while abs(result - x) > eps:
    x = result
    result = x - formula(x) / df

print('Result:', result)
