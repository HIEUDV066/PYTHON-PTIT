a = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
b = []
c = []
max1 = 0
for i in a:
	b.append(a.count(i))
	if a.count(i)>max1:
		max1=a.count(i)
for i in range(len(b)):
	if b[i]==max1:
		c.append(a[i])
print("Muc co so lan xuat hien toi da cua danh sach:")
print(c[0], end= ' ')
for i in range(1,len(c)):
	if c[i]!=c[i-1]:
		print(c[i],end=' ')
print()