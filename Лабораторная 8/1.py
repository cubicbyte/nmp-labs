import matplotlib.pyplot as plt

from math import factorial as fact

x=[0.47, 0.48, 0.49, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55]
y=[18.9425, 18.1746, 17.3010, 16.3123, 15.1984, 13.9484, 12.5508, 10.9937, 9.2647]

diff = x[1] - x[0]

x1 = 0.473
x2 = 0.551
q = (x1 - x[0]) / diff
q1 = (x2 - x[-1]) / diff

def formula(y, j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j-=1
        return formula(mas, j)

f1 = y[0] + q * formula(y, 1)[0] + q * (q-1) * formula(y, 2)[0] / fact(2)
f2 = q * (q-1) * (q-2) * formula(y, 3)[0] / fact(3)
f3 = q * (q-1) * (q-2) * (q-3) * formula(y, 4)[0] / fact(4)
f4 = q * (q-1) * (q-2) * (q-3) * (q-4) * formula(y, 5)[0] / fact(5)

res = f1 + f2 + f3 + f4

print('Result:', round(res, 5))

plt.grid(True)
plt.title('Результат графіка')

plt.plot(y, x, 'o', linestyle='solid')
plt.show()
