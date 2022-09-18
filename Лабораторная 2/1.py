
ACCURACY = 0.0001

def formula(x):
    return 4 * pow(x, 4) + 4 * pow(x, 3) - 6 * pow(x, 2) - 9 * x - 1



segment = 0, 100

while True:
    x = (segment[0] + segment[1]) / 2

    segment_1 = segment[0], x
    segment_2 = x, segment[1]
    
    result_1 = formula(segment_1[0]), formula(segment_1[1])
    result_2 = formula(segment_2[0]), formula(segment_2[1])
    
    if result_1[0] > 0 > result_1[1] or result_1[0] < 0 < result_1[1]:
        segment = segment_1
        if result_1[1] <= ACCURACY or result_1[1] <= ACCURACY:
            break

    else:
        segment = segment_2
        if result_2[1] <= ACCURACY or result_2[1] <= ACCURACY:
            break

print(segment)
