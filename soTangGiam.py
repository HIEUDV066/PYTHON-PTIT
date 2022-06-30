t = int(input())
while t != 0:
	s = input()
	if(len(s)<=3):
		print("NO")
	else:
		test = 1
		i = 0
		while test==1:
			if(s[i+1]>s[i]):
				i += 1
			else:
				test = 0
		count = 0
		for j in range(i,len(s)-1):
			if s[j+1]>=s[j]:
				count += 1
		if(count != 0):
			print("NO")
		else:
			print("YES")
	t -= 1