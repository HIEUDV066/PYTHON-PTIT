a = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
b = []
for i in a[0]:
	count = 0
	for j in range(1,len(a)):
		if i in a[j]:
			count +=1
		if count == len(a)-1:
			b.append(i)
print(b)