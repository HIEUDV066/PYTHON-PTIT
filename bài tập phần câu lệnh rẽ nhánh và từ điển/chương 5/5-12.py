dic = dict(hieu=1,nam=5,huy=2,tu=7)
dic2 = dict(lin = 8, hieu=10)
dic.update(dic2)
for i in dic:
	print(i," thich so: ",dic[i])