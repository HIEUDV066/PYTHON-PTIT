t = int(input())
while t != 0:
	n = int(input())
	sum1 = 0
	sum2 = 0
	i = 1
	while i <= n:
		if(i%2 == 1 ):
			sum1 += 1/i
		else:
			sum2 += 1/i
		i += 1
	if(n%2==1):
		print('{0:.{1}f}'.format(sum1, 6))
	else:
		print('{0:.{1}f}'.format(sum2, 6))
	t -= 1