line  = input()
k = int(input())
arr = []
n = len(line)
if(len(line) % 2 == 1):
    n -= 1

for i in range(0,n,2):
    arr.append(int(line[i:i+2]))
dic = dict()
dem = 0
for i in arr:
    dic[i]=0
for i in arr:
    dic[i] +=1
a = sorted(dic.items(), key = lambda x:x[0], reverse=False)
t = 0
for i in a:
    if i[1]>=k:
        print(i[0], i[1])
        t +=1
if t == 0:
    print("NOT FOUND")