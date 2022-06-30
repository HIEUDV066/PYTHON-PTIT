import math
def snt(n):
	if n<2:
		return False
	else:
		for i in range(2, int(math.sqrt(n)+1)):
			if n%i==0:
				return False
		return True
n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in a:
	if snt(i):
		b.append(i)
b.sort()
dem = 0
for i in range(len(a)):
	if snt(a[i]):
		a[i]=b[dem]
		dem +=1
for i in a:
	print(i, end=' ')