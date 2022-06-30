import re
a = [int(i) for i in input().split()]
n = a[0]
k = a[1]
s = []
while n!=0:
	n -=1
	line = input().lower()
	tmp = re.findall(r'\w+',line)
	s +=tmp
s.sort()
dic = dict()

for i in s:
	if i in dic:
		dic[i] += 1
	else:
		dic[i] = 1
dic_sort = sorted(dic.items(), key = lambda x:x[1], reverse=True)
for i in dic_sort:
	if(i[1]>=k):
		print(i[0], i[1])