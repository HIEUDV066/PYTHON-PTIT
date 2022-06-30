def isPrime(num):
    if num > 1:
        for i in range( 2 , int(num / 2) + 1):
            if  (num % i == 0):
                return 0
    else:
        return 0
    return 1
line = input().split()
n = int(line[0])
m = int(line[1])
a = [[int(j) for j in input().split()] for i in range(n)]
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()