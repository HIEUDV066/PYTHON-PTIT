def inkq():
	for i in range(1,k+1):
		print(b[a[i]-1],end=' ')
	print()
def Try(i):
	for j in range(a[i-1]+1,n-k+i+1):
		a[i]=j;
		if i==k:
			inkq()
		else:
			Try(i+1)

a = [0]*50
n, k = map(int, input().split())
b = [int(i) for i in input().split()]
b.sort()
i=0
while i<len(b)-1:
	if b[i+1]==b[i]:
		b.pop(i+1)
	else:
		i +=1
n=len(b)
Try(1)
	