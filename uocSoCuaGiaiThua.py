def uoc(n,p):
	res = 0
	while n!=0:
		n /= p
		res +=int(n) 
	return res
t = int(input())
while t!=0:
	t -=1
	line = [int(i) for i in input().split()]
	print(uoc(line[0],line[1]))