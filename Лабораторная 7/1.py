arr_x = [2.4, 2.6, 2.8, 3.0, 3.2, 3.4]
arr_y = [3.526, 3.782, 3.945, 4.043, 4.104, 4.155]
diff = arr_x[1] - arr_x[0]

print('Diff =', diff)

arr_1 = []
arr_2 = []
arr_3 = []
arr_4 = []



# Скінченні різниці 1-го порядку
for i, num in enumerate(arr_y):
    arr_1.append(num - arr_y[i - 1])

arr_1.pop(0)
print('arr_1 =', arr_1) 



# Скінченні різниці 2-го порядку
for i, num in enumerate(arr_1):
    arr_2.append(num - arr_1[i - 1])

arr_2.pop(0)
print('arr_2 =', arr_2)



# Скінченні різниці 3-го порядку
for i, num in enumerate(arr_2):
    arr_3.append(num - arr_2[i - 1])

arr_3.pop(0)
print('arr_3 =', arr_3)



# Скінченні різниці 4-го порядку
for i, num in enumerate(arr_3):
    arr_4.append(num - arr_3[i - 1])

arr_4.pop(0)
print('arr_4 =',arr_4)



y1 = 1 / diff * (arr_1[1] - (arr_2[1] / 2) + (arr_3[1] / 3) - (arr_4[1] / 4))
y2 = 1 / (diff ** 2) * (arr_2[1] - arr_3[1] + 11 / 12 * arr_4[1])

print('y1 =', y1)
print('y2 =', y2)
