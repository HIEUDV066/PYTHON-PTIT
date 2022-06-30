t = int(input())
while t != 0:
	s = input()
	l = len(s)
	if int(s[l - 1]) == 6 and int(s[l - 2]) == 8:
		print("YES")
	else:
		print("NO")
	t -= 1