n = int(input())
arr = [float(i) for i in input().split()]
arr.sort()
tong = 0
count = 0
for i in range(len(arr)):
	if arr[i]!=arr[0] and arr[i]!=arr[len(arr)-1]:
		tong += arr[i]
		count +=1
tb = tong/count
print("{:.2f}".format(round(tb,2)))