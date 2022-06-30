line  = input()
arr = []
n = len(line)
if(len(line) % 2 == 1):
    n -= 1

for i in range(0,n,2):
    arr.append(line[i:i+2])
dic = dict()
dem = 0
for i in arr:
    dic[i]=1
for i in dic:
    print(i, end=' ')