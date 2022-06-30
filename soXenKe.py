t = int(input())
while t != 0:
	s = input()
	count = 0
	if(len(s)%2==0):
		print("NO")
	else:
		if s[0]==s[1]:
			print("NO")
		else:
			for i in range(0,len(s),2):
				if s[i]!=s[0]:
					count += 1
			if count!=0:
				print("NO")
			else:
				print("YES")
	t -= 1