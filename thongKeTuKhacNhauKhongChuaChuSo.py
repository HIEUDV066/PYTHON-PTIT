import re
n = int(input())
s = []
while n!=0:
	n -=1
	nhap = input().lower()
	line = ''.join(i for i in nhap if not i.isdigit())
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
	print(i[0], i[1])