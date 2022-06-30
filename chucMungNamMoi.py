import collections
n = int(input())
s = []
for i in range(1,n+1):
	c = input()	
	if s.count(c)==0:
		s.append(c)
print(len(s))