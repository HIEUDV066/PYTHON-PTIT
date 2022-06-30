t = int(input())
while t!= 0:
	s = input()
	tong = 0
	tich = 1
	for i in range(len(s)):
		if i%2==1:
			tong += int(s[i])
		else:
			if s[i]!='0':
				tich = tich*int(s[i])
	print(tich, tong, end=" ")
	print()
	t -= 1