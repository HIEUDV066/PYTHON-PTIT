t = int(input())
while t != 0:
	s = input()
	i = 0
	count = 1
	r = ''
	while i < len(s)-1:
	    if(s[i] == s[i+1]):
	    	count += 1
	    else:
	    	print(count, s[i], sep='', end='') 
	    	count = 1
	    i += 1
	print(count, s[len(s)-1], sep='', end='')
	print()
	t -= 1