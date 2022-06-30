import datetime
class NguoiChoi:
    def __init__(self, id, ten, gioVao, gioRa):
        self.id = id
        self.ten = ten
        self.gioVao = gioVao
        self.gioRa = gioRa
    def tinhTime(self):
        timeIn = datetime.datetime.strptime(self.gioVao,'%H:%M')
        timeOut = datetime.datetime.strptime(self.gioRa, '%H:%M')
        self.time = timeOut - timeIn
    def result(self):
        self.time = str(self.time)
        a = [int(i) for i in self.time.split(':')]
        print( "{} {} {} gio {} phut".format(self.id,self.ten,a[0],a[1]))
data = []
t = int(input())
for i in range(t):
    nc = NguoiChoi(input(), input(), input(), input())
    nc.tinhTime()
    data.append(nc)
data = sorted(data, key=lambda x:x.time, reverse=True)
for i in data:
    i.result()

