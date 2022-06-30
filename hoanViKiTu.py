import itertools
s= input()
a=list(itertools.permutations(s))
for i in a:
	for j in range(len(i)):
		print(i[j], end='')
	print()