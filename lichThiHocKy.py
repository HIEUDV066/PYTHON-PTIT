from datetime import datetime
dic = dict()
class LichThi():
    def __init__(self,id,ma, ngay, gio, nhom):
        self.id = id
        self.ma = ma
        self.ngay = datetime.strptime(ngay,"%d/%m/%Y")
        self.gio = datetime.strptime(gio,"%H:%M")
        self.nhom = nhom
    def timTen(self):
        for i in dic:
            if self.ma == dic[i]:
                self.ten = i
    def __str__(self):
        if self.id <10:
            return f'T00{self.id} {self.ma} {self.ten} {self.ngay.strftime("%d/%m/%Y")} {self.gio.strftime("%H:%M")} {self.nhom}'
        else:
            return f'T0{self.id} {self.ma} {self.ten} {self.ngay.strftime("%d/%m/%Y")} {self.gio.strftime("%H:%M")} {self.nhom}'
n, m = [int(i) for i in input().split()]
for i in range(n):
    dic[input()] = input()
data = []
for i in range(m):
    a = [i for i in input().split()]
    lt = LichThi(i+1, a[0], a[1], a[2], a[3])
    lt.timTen()
    data.append(lt)
data = sorted(data, key= lambda x:(x.ngay,x.gio,x.ma))
for i in data:
    print(i)