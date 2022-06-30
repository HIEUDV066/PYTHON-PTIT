import math


def convert(n):
    if 3 <= n <= 4:
        return 2.5
    elif 5 <= n <= 6:
        return 3.0
    elif 7 <= n <= 9:
        return 3.5
    elif 10 <= n <= 12:
        return 4.0
    elif 13 <= n <= 15:
        return 4.5
    elif 16 <= n <= 19:
        return 5.0
    elif 20 <= n <= 22:
        return 5.5
    elif 23 <= n <= 26:
        return 6.0
    elif 27 <= n <= 29:
        return 6.5
    elif 30 <= n <= 32:
        return 7.0
    elif 33 <= n <= 34:
        return 7.5
    elif 35 <= n <= 36:
        return 8.0
    elif 37 <= n <= 38:
        return 8.5
    elif 39 <= n <= 40:
        return 9.0
    else:
        return 1.0


testCase = int(input())
while testCase > 0:
    val = [float(x) for x in input().split()]
    listenPoint = convert(int(val[1]))
    readPoint = convert(int(val[0]))
    res = (listenPoint + readPoint + val[2] + val[3]) / 4
    soLe = res - int(res)
    #if soLe == 0.25 or soLe == 0.75:
        #print(res + 0.25)
    if  0 <= soLe < 0.25:
        print(round(math.floor(res), 1) / 10 * 10)
    elif 0.25 <= soLe < 0.75:
        print(round(math.floor(res), 1) / 10 * 10 + 0.5)
    else:
        print(round(math.ceil(res), 1)/10 * 10)
    testCase -= 1

'''
2
15 25 5.0 5.5
22 32 6.0 6.0
'''