n = int(input())
a = []
count = 0
while count<n:
    line = input()
    line = line.split()
    for i in line:
        count +=1
        a.append(int(i))
a_chan = []
a_le = []
dic = dict()
for i in range(n):
    if a[i]%2==0:
        dic[i] = 0
        a_chan.append(a[i])
    else:
        dic[i] = 1
        a_le.append(a[i])
a_chan.sort()
a_le.sort(reverse=True)
count1 = 0
count2 = 0
for i in dic:
    if dic[i]==0:
        a[i] = a_chan[count1]
        count1 +=1
    else:
        a[i] = a_le[count2]
        count2 +=1
print("")
for i in a:
    print(i,"",end="")