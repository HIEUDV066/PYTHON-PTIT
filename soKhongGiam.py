t = int(input())
while t!=0:
	n = input()
	count = 0
	for i in range(len(n)-1):
		if int(n[i]) > int(n[i+1]):
			count +=1
	if(count != 0):
		print("NO")
	else:
		print("YES")
	t -=1