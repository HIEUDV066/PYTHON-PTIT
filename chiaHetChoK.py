a, K, N = map(int, input().split())
res = -1
N = (N//K) +1
for i in range(N):
	x = i*K-a
	if x > 0:
		res = 1
		print(x, end=' ')
if res==-1:
	print("-1")