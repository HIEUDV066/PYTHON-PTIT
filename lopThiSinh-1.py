class sinhVien:
	def __init__(self, ten, ngaySinh, diem1, diem2, diem3):
		self.ten = ten
		self.ngaySinh = ngaySinh
		self.diem1 = diem1
		self.diem2 = diem2
		self.diem3 = diem3		
if __name__== '__main__':
	a = []
	for i in range(5):
		ip = input()
		a.append(ip)
	sv = sinhVien(a[0], a[1], float(a[2]), float(a[3]), float(a[4]))
	print(sv.ten, sv.ngaySinh, sv.diem1+sv.diem2+sv.diem3)