s = input()
res = ''
count = 0
l = len(s)-1
while l >= 0:
	if(count == 3):
		res = ',' + res
		count = 0
	count += 1
	res = s[l] + res
	l -=1
print(res)