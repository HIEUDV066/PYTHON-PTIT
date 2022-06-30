t = 1
while t==1:
	a = [int(i) for i in input().split()]
	if a.count(0)==4:
		break
	else:
		count = 0
		while not(a[0]==a[1] and a[1]==a[2] and a[2]==a[3]):
			k = a[0]
			for i in range(len(a)-1):
				a[i] = abs(a[i]-a[i+1])
			a[3] = abs(a[3]-k)
			count += 1
		print(count)