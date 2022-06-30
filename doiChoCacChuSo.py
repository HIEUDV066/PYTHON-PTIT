t = int(input())
while t!=0:
	t -=1
	a = input()
	n=[]
	for i in a:
		n.append(i)
	if len(n)==1:
		print("-1")
	else:
		k = len(n)-2
		while k >= 0 and n[k]<=n[k+1]:
			k -=1
		if k<0:
			print("-1")
		else:		
			max1 = k+1
			for j in range(k+1,len(n)):
				if n[j]<n[k] and n[j]>n[max1]:
					max1 = j
			n[k], n[max1] = n[max1], n[k]
			if n[0]=='0':
				print("-1")
			else:
				for i in n:
					print(i, end='')
				print()