import math
def object(tu, mau):
		return phanSo(tu, mau)
class phanSo:
	
	def __init__(self , tu, mau):
		self.tu = tu
		self.mau = mau
	def rutGon(self):
		ucln = math.gcd(self.tu, self.mau)
		self.tu = self.tu/ucln
		self.mau = self.mau/ucln
	def add(self, phanSo):
		mau = self.mau*phanSo.mau
		tu = self.tu*phanSo.mau + phanSo.tu*self.mau
		return object(tu,mau)
	def __str__(self):
		return "{}/{}".format(int(self.tu), int(self.mau))
a = input().split()
ps1 = phanSo(int(a[0]), int(a[1]))
ps2 = phanSo(int(a[2]), int(a[3]))
ps3 = ps1.add(ps2)
ps3.rutGon()
print(ps3)