line = [int(i) for i in input().split()]
n, m = line[0], line[1]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
set1 = set(a)
set2 = set(b)
arr1 = sorted(set1)
arr2 = sorted(set2)
t = True
for i in range(len(arr1)):
	if arr1[i]!=arr2[i]:
		print("NO")
		t = False
		break
if t==True:
	print("YES")