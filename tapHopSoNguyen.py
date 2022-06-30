line = [int(i) for i in input().split()]
n, m = line[0], line[1]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
set1 = set(a)
set2 = set(b)
set3 = set1 & set2
set4 = set1 - set2
set5 = set2 - set1
arr1 = sorted(set3)
arr2 = sorted(set4)
arr3 = sorted(set5)
for i in arr1:
	print(i, end=' ')
print()
for i in arr2:
	print(i, end=' ')
print()
for i in arr3:
	print(i, end=' ')