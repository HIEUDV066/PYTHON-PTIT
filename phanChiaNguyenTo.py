import math
def isPrime(n):
    if n<2: return 0
    for i in range(2,int( math.sqrt(n) + 1 )):
        if n % i ==0: return 0
    return 1

n = int(input())
line = input().split()
hash = dict()

for i in range(len(line)):
    line[i] = int(line[i])
    if line[i] in hash:
        continue
    else:
        hash[line[i]] = 1

sumR = 0
sumL = 0
dem = 0
not_found = 1

for key in hash:
    sumR += key
for key in hash:
    sumL += key
    sumR -= key
    if isPrime(sumL) and isPrime(sumR):
        not_found = 0
        break;
    dem += 1
if not_found:
    print("NOT FOUND")
else:
    print(dem)