import math
class HoaDon:
    def __init__(self, id, ten, csCu, csMoi):
        self.id = id
        self.ten = ten
        self.csCu = csCu
        self.csMoi = csMoi
    def tinhTien(self):
        sum1 = 0
        a = self.csMoi - self.csCu
        if a <= 50:
            sum1 = 100*a
            self.tien = sum1 + sum1*0.02
        if 50<a<=100:
            sum1 = 50*100 + (a-50)*150
            self.tien = sum1 + sum1 * 0.03
        if a>100:
            sum1 = 50*100 + 50*150 + (a-100)*200
            self.tien = sum1 + sum1 * 0.05
    def __str__(self):
        if self.id < 10:
            return "KH0{} {} {}".format(self.id, self.ten, math.ceil(self.tien))
        else:
            return "KH{} {} {}".format(self.id, self.ten, math.ceil(self.tien))
data = []
t = int(input())
for i in range(t):
    hd = HoaDon(i+1,input(),int(input()),int(input()))
    hd.tinhTien()
    data.append(hd)
data=sorted(data,key=lambda x:x.tien,reverse=True)
for i in data:
    print(i)
