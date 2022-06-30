t = int(input())
while t!=0:
	t -=1
	n = int(input())
	arr = [int(i) for i in input().split()]
	dic = dict()
	for i in arr:
		if i in dic:
			dic[i] += 1
		else:
			dic[i] = 1
	max1 = 0
	for key in dic:
		if dic[key]>n/2 and dic[key]>max1:
			max1 = dic[key]

	if max1!=0:
		min1 = 1000001
		for key in dic:
			if dic[key]==max1:
				if key<min1:
					min1 = key
		print(min1)
	else:
		print("NO")