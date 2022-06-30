t = int(input())
while t!=0:
	n, d= map(int, input().split())
	s = [int(i) for i in input().split()]
	for i in range(d,n):
		print(s[i], end=' ')
	for i in range(d):
		print(s[i],end=' ')
	print()
	t -= 1