def check(s):
	sum = 0
	for i in range(0, len(s)-1, 1):
		sum = sum + int(s[i])
		if abs(int(s[i+1]) - int(s[i])) != 2:
			return False
	sum = sum + int(s[-1])
	if (sum%10)!=0:
		return False
	return True
t = int(input())
while t != 0:
	s = input()
	if(check(s) == True):
		print("YES")
	else:
		print("NO")
	t -= 1 