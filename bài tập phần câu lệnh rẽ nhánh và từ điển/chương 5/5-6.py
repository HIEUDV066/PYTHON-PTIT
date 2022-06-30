favorite_languages=dict(hieu='co',linh='khong',huy='co',duy='khong')
a = []
for i in favorite_languages:
	if favorite_languages[i]=='co':
		a.append(i)
		print('cam on',i,'da tham gia')
	else:
		print('moi ban',i,'tham gia')
