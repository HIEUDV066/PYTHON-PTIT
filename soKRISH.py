def giaiThua(n):
	gt = 1
	for i in range(1,n+1,1):
		gt *= i
	return gt 
t = int(input())
while t!=0:
	s = input()
	tong = 0
	for i in range(len(s)):
		tong += giaiThua(int(s[i]))
	if tong==int(s):
		print("Yes")
	else:
		print("No")
	t -=1