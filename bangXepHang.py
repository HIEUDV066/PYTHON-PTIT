class SinhVien:
	def __init__(self,ten,baiDung,submit):
		self.ten = ten
		self.baiDung = baiDung
		self.submit = submit
	def __str__(self):
		return "{} {} {}".format(self.ten,self.baiDung,self.submit)
data = []
t = int(input())
for i in range(t):
	name = input()
	a = [int(j) for j in input().split()]
	sv = SinhVien(name, a[0], a[1])
	data.append(sv)
data = sorted(data, key = lambda x:(x.baiDung*(-1),x.submit,x.ten))
for i in data:
	print(i)