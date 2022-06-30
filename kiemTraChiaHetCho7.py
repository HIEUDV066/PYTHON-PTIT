t = int(input())
while t!=0:
	n = int(input());
	if(n%7==0):
		print(n)
	else:
		t1 = 1000
		while t1 != 0:
			n1 = str(n)
			n1 = n1[::-1]
			n += int(n1)
			if(n%7==0):
				print(n)
				break
			t1 -=1
	t -= 1
