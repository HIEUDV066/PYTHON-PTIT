t = int(input())
while t!= 0:
	s = input()
	tong = 0
	tich = 1
	count = 0
	for i in range(len(s)):
		if i%2==0:
			tong += int(s[i])
		else:
			if s[i]=='0':
				count += 1
			else:
				tich = tich*int(s[i])
	if count==len(s)//2:
			print(tong, "0", end=" ")
	else:
			print(tong, tich, end=" ")
	print()
	t -= 1