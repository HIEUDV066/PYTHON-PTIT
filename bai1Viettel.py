N, X = map(int, input().split())
a = [int(i) for i in input().split()] 
sum = 0
i = 0
while sum<=X:
	sum = sum + a[i]
	i = i+1
print(i, end='')