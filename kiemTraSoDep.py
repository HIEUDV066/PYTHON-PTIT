t = int(input())
while t != 0:
	s = input()
	count = 0
	for i in range(len(s)):
		if i%2==0 and s[i]!=s[0]:
			count += 1
		if i%2==1 and s[i]!=s[1]:
			count += 1
	if(count != 0):
		print("NO")
	else:
		print("YES")
	t -= 1