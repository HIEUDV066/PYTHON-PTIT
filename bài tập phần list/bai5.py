a = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
count1 = 0
for i in a:
	if a.count(i)>1:
		count1 +=1
if count1>0:
	print("False")
else:
	print("True")