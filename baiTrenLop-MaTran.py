def tong(a):
	tong1 = 0
	for i in a:
		tong1 = tong1+i 
	return tong1
a = [[int(i) for i in input().split() ] for j in range(3)]
b = sorted(a,key = tong)
print(b)