t = int(input())
while t != 0:
	val = input()
	sum = 0
	for i in val:
		if(i != '4' and i != '7'):
			sum +=1
	if sum == 0:
		print("YES")
	else:
		print("NO")
	t -=1