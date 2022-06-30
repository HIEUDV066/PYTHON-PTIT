t = int(input())
while t!=0:
	t -=1
	n = int(input())
	arr = []
	dic = dict()
	while n!=0:
		n -=1
		arr.append(input())
	for i in arr:
		if i in dic:
			dic[i] +=1
		else:
			dic[i] = 1
	max1 = 0
	for key in dic:
		if dic[key] > max1:
			max1 = dic[key]
	min1 = 1001
	for key in dic:
		if dic[key] == max1:
			if int(key) < min1:
				min1 = int(key)
	print(min1)