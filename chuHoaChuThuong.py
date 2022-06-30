val = input()
hoa = val.upper()
thuong = val.lower()
count1 = 0
count2 = 0
for i in range(len(val)):
	if(val[i] != hoa[i]):
		count1 += 1
	if(val[i] != thuong[i]):
		count2 +=1
if(count1 < count2):
	print(hoa)
else:
	print(thuong)