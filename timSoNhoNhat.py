import re
t = int(input())
while t != 0:
	s = input()
	res = []
	res = re.split(r"\D+",s)
	k = int(res[1])
	max1 = k
	for i in res:
		if i!='':
			max1 = max(int(i),k)
			k = max1
	print(max1)
	t -= 1