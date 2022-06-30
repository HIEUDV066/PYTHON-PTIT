ngay = [[20,18,1,2],[19,20,2,3],[21,19,3,4],[20,20,4,5],[21,20,5,6],[21,22,6,7],[23,22,7,8],[23,22,8,9],[23,22,9,10],[23,22,10,11],[23,21,11,12],[22,19,12,1]]
cung = ['Bao Binh','Song Ngu','Bach Duong','Kim Nguu','Song Tu','Cu Giai','Su Tu','Xu Nu','Thien Binh','Thien Yet','Nhan Ma','Ma Ket']

t = int(input())
while t!= 0:
	n1, n2 = map(int, input().split())
	if n1>=ngay[n2-1][0]:
		print(cung[n2-1])
	else:
		print(cung[n2-2])
	t -= 1