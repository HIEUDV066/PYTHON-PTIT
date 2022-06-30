def tong(a):
	tong1 = 0
	for i in a:
		tong1 = tong1+i 
	return tong1
a = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
b = sorted(a,key = tong)
print(b)