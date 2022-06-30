import math

prime_set = [2,3,5,7]
num = 11
count = 0

for i in range(11,10000):
    flag = 1
    for j in prime_set:
        if(i % j == 0):
            flag = 0
            break
    if flag:
        prime_set.append(i)
        count += 1
        if count > 1100:
            break
a = [int(i) for i in input().split()]
n, x = a[0], a[1]
for i in range(n+1):
    print(x, end=' ')
    x +=prime_set[i]