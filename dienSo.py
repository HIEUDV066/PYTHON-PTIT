t = int(input())
while t!=0:
	n = int(input())
	a = [int(i) for i in input().split()]
	a.sort()
	set1=set(a)
	print(a[-1]-a[0]+1-len(set1))
	t-=1