
def formula(x):
    return 4 * pow(x, 4) + 4 * pow(x, 3) - 6 * pow(x, 2) - 9 * x - 1

a = 0
b = 100
eps = 0.001

while True:
    x = (a + b) / 2
    seg_1 = a, x
    seg_2 = x, b
    result_1 = formula(seg_1[0]), formula(seg_1[1])
    result_2 = formula(seg_2[0]), formula(seg_2[1])
    
    if result_1[0] > 0 > result_1[1] or result_1[0] < 0 < result_1[1]:
        a = seg_1[0]
        b = seg_1[1]
        if result_1[1] <= eps or result_1[1] <= eps:
            break

    else:
        a = seg_2[0]
        b = seg_2[1]
        if result_2[1] <= eps or result_2[1] <= eps:
            break

result = a

print('Result:', result)
