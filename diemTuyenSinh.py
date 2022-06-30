class ThiSinh:
    def __init__(self,id,ten,diemThi,danToc,khuVuc):
        self.id = id
        self.ten = ten
        self.diemThi = diemThi
        self.danToc = danToc
        self.khuVuc = khuVuc
    def tinhDiem(self):
        tong = self.diemThi
        if self.khuVuc==1:
            tong = tong + 1.5
        if self.khuVuc==2:
            tong = tong + 1
        if self.danToc != 'Kinh':
            tong = tong + 1.5
        self.diem = tong
    def trangThai(self):
        if self.diem >= 20.05:
            self.tt = 'Do'
        else:
            self.tt = 'Truot'
    def __str__(self):
        if self.id < 10:
            return "TS0{} {} {} {}".format(self.id,self.ten, self.diem, self.tt)
        else:
            return "TS{} {} {} {}".format(self.id, self.ten, self.diem, self.tt)
data = []
t = int(input())
for i in range(t):
    name = input().strip()
    tmp = name.split()
    name = ' '.join(tmp).strip().title()
    ts = ThiSinh(i+1, name, float(input()), input(), int(input()))
    ts.tinhDiem()
    ts.trangThai()
    data.append(ts)
data = sorted(data, key= lambda x:x.diem, reverse=True)
for i in data:
    print(i)