t = int(input())
while t != 0:
	N, X, M = map(float, input().split())
	count = 0
	while N < M:
		N = N + N*X*0.01
		count +=1
	print(count)
	t -=1