import math
class phanSo:
	def __init__(self , tu, mau):
		self.tu = tu
		self.mau = mau
a = input().split()
ps = phanSo(int(a[0]), int(a[1]))
ucln = math.gcd(ps.tu, ps.mau)
print(ps.tu//ucln,'/',ps.mau//ucln,sep='')