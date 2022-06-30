def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
n = int(input())
a = [input() for i in range(n)]
ces = 0
for i in range(n):
    count = 0
    for j in a[i]:
        if j=='C':
            count +=1
    if count>=2:
        ces += (giaiThua(count))//(giaiThua(count-2)*giaiThua(2))
for i in range(n):
    count = 0
    for j in range(n):
        if a[j][i]=='C':
            count +=1
    if count>=2:
        ces += (giaiThua(count))//(giaiThua(count-2)*giaiThua(2))
print(ces)