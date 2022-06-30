t = int(input())
while t!=0:
	n = input()
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]
	a.sort()
	b.sort()
	k = True
	for i in range(0,len(a)):
		if a[i]>b[i]:
			print("NO")
			k = False
			break
	if k == True:
		print("YES")
	t -=1