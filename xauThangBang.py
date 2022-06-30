t = int(input())
while t!=0:
	s = input()
	s1 = s[::-1]
	count = 0
	for i in range(len(s)-1):
		if abs(ord(s[i])-ord(s[i-1]))!=abs(ord(s1[i])-ord(s1[i-1])):
			count += 1
	if count==0:
		print("YES")
	else:
		print("NO")
	t -= 1