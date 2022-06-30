curent_users=['admin','Linh','Anh','Hue123','Huycps']
for i in curent_users:
	i.lower()
new_users=['Chien21','Linh','Anh23','Hue123']
ok=0
for i in curent_users:
	ok=0
	for j in new_users:
		if j==i:
			print(' Ten nguoi dung nay da duoc su dung: '+j)
			ok=1
			break
	if ok==0:
		print('Ten nguoi dung kha dung: '+i)
