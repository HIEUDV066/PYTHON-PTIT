t = int(input())
while t!=0:
	s = input()
	count = 0
	for i in s:
		if not(i=='0' or i=='1' or i=='2'):
			count += 1
	if(count != 0):
		print("NO")
	else:
		print("YES")
	t -= 1