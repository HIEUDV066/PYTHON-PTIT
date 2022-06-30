def check(n):
	n1 = n[::-1]
	if(len(n)%2!=0):
		return False
	if n!=n1:
		return False
	for i in n:
		if(int(i)%2!=0):
			return False
	return True
t = int(input())
while t!= 0:
	s = int(input())
	for i in range(22,s,22):
		if(check(str(i))==True):
			print(i, end=' ')
	print()
	t -= 1