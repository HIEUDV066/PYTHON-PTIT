N = int(input())
s = input()
Q = int(input())
while Q!=0:
	t, a, b = map(int, input().split())
	if t == 2:
		s = s[N:]+s[0:N]
	else:
		s = '0' + s
		s = s[1:a] + s[b] + s[(a+1):b] + s[a] + s[(b+1):]
	Q = Q-1
print(s) 