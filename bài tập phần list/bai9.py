a = [[int(i) for i in input().split() ] for j in range(3)]
n = int(input("Xoa cot thu: "))
for i in a:
	i.pop(n-1)
print(a)