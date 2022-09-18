from math import sqrt


a1 = sqrt(75)
a2 = 51 / 11

b1 = 8.66
b2 = 4.64

acc1 = abs(a1 - b1)
acc2 = abs(a2 - b2)

print('Рівність 1 точніша' if acc1 < acc2 else 'Рівність 2 точніша')
