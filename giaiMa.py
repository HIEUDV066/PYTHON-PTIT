t = int(input())
while t != 0:
	s = input()
	r ='';
	i = 0
	while i < len(s)/2:
		r = r + s[i*2]*int(s[i*2+1])
		i += 1
	print(r)
	t -=1