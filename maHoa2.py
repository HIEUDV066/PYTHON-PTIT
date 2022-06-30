t = 1
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while t != 0:
	nhap = [str(i) for i in input().split()]
	k = int(nhap[0])
	if k == 0:
		break
	s = nhap[1]
	res = ""
	for i in s:
		index = p.find(i)
		res = p[(index+k)%28] + res
	print(res) 