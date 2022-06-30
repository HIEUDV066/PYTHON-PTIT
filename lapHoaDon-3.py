class HoaDon:
    def __init__(self,id,ten,soLuong,donGia,chietKhau):
        self.id = id
        self.ten = ten
        self.soLuong = soLuong
        self.donGia = donGia
        self.chietKhau = chietKhau
    def tinhTien(self):
        self.tien = self.donGia*self.soLuong - self.chietKhau
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.id, self.ten,self.soLuong,self.donGia,self.chietKhau,self.tien)
data = []
t = int(input())
for i in range(t):
    hd = HoaDon(input(),input(), int(input()),int(input()), int(input()))
    hd.tinhTien()
    data.append(hd)
data = sorted(data, key = lambda x:x.tien, reverse=True)
for i in data:
    print(i)