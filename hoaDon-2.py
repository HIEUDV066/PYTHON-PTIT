import datetime
class Hoadon:
    def __init__(self,name,phong,start,end,chiphiphatsinh,ma):
        self.name=name
        self.phong=phong
        self.start=start
        self.end=end
        self.chiphiphatsinh=chiphiphatsinh
        self.ma='KH%02d'%ma
        self.day=0
        self.tongtien=0
    def tinhNgay(self):
        if self.start == self.end:self.day=1;return
        time_in=datetime.datetime.strptime(self.start,'%d/%m/%Y')
        time_out=datetime.datetime.strptime(self.end,'%d/%m/%Y')
        dis=str(time_out-time_in)
        dis=[i for i in dis.split(" ")]
        self.day=int(dis[0])+1
    def tinhTien(self):
        if self.phong[0] == '1': self.tongtien = self.day * 25 + self.chiphiphatsinh
        if self.phong[0] == '2': self.tongtien = self.day * 34 + self.chiphiphatsinh
        if self.phong[0] == '3': self.tongtien = self.day * 50 + self.chiphiphatsinh
        if self.phong[0] == '4': self.tongtien = self.day * 80 + self.chiphiphatsinh
    def __str__(self):
        return "{} {} {} {} {}".format(self.ma, self.name, self.phong, self.day, self.tongtien)
lst=[]
for i in range(int(input())):
    name=input().strip()
    phong=input()
    start=input().strip()
    end=input().strip()
    chiphiphatsinh=int(input().strip())
    lst.append(Hoadon(name,phong,start,end,chiphiphatsinh,i+1))
for i in lst:
    i.tinhNgay()
    i.tinhTien()
lst=sorted(lst,key=lambda x: x.tongtien,reverse=True)
for i in lst:
    print(i)