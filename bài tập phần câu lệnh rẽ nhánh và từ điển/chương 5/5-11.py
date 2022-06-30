HaNoi = dict(quoc_gia='Viet Nam',dan_so='90tr',dien_tich='1000km')
HCM = dict(quoc_gia='Viet Nam',dan_so='100tr',dien_tich='2000km')
DaNang = dict(quoc_gia='Viet Nam',dan_so='50tr',dien_tich='800km')
cities = dict(Ha_noi=HaNoi,H_C_M=HCM,Da_Nang=DaNang)
for i in cities:
	print(i,cities[i])