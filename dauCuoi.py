t = int(input())
while t != 0:	
	val = input()
	so1 = val[0] + val[1]
	so2 = val[-2] + val[-1]
	if so1== so2:
		print("YES")
	else:
		print("NO")
	t -=1