s1 = [i.lower() for i in input().split()]
s2 = [i.lower() for i in input().split()]
set1={i for i in s1}
s3, s4 = [],[]
set2 = set()
for i in s2:
	if (i in s1)==False:
		set1.add(i)
	else:
		set2.add(i)
while len(set1)!=0:
	s3.append(set1.pop())
while len(set2)!=0:
	s4.append(set2.pop())
s3.sort()
s4.sort()
for i in s3:
	print(i, end=' ')
print()
for i in s4:
	print(i, end=' ')