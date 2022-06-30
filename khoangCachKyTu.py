t = int(input())
while t != 0:
	s = input()
	r = s[::-1]
	i = 1
	count = 0
	while i < len(s):
		if abs(ord(s[i]) - ord(s[i-1]))!=abs(ord(r[i]) - ord(r[i-1])):
			count +=1
		i += 1
	if(count != 0):
		print("NO")
	else:
		print("YES")
	t -= 1
