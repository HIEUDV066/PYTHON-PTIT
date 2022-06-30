line  = input()
arr = []
n = len(line)
if(len(line) % 2 == 1):
    n -= 1

for i in range(0,n,2):
    arr.append(line[i:i+2])
set1 = set(arr)
res = sorted(set1)
for i in res:
    print(i,end= " ")