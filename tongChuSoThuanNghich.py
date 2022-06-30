def thuanNghich(n):
	s = n[::-1]
	if(s == n):
		return True
	else:
		return False
t = int(input())
while t != 0:
	n = input()
	tong = 0
	for i in n:
		tong += int(i)
	tong2 = str(tong)
	if thuanNghich(tong2)==True and len(tong2) > 1:
		print("YES")
	else:
		print("NO")
	t -= 1