n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
k = int(input())
tong1 = 0
tong2 = 0
for i in range(1,n):
	for j in range(0,i):
		tong1 += a[i][j]
		tong2 += a[-i-1][-j-1]
hieu = abs(tong1 - tong2)
if hieu<=k:
	print("YES")
else:
	print("NO")
print(hieu)