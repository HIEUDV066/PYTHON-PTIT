class GiaoVien:
    def __init__(self,id, ten,ma,diemTin, diemMon):
        self.id = id
        self.ten = ten
        self.ma = ma
        self.diemTin = diemTin
        self.diemMon = diemMon
    def tinhDiem(self):
        d = self.diemTin*2 + self.diemMon
        if self.ma[1]=='1':
            self.diem = d + 2.0
        if self.ma[1] == '2':
            self.diem = d + 1.5
        if self.ma[1] == '3':
            self.diem = d + 1.0
        if self.ma[1] == '4':
            self.diem = d + 0.0
    def xetMon(self):
        if self.ma[0]=='A':
            self.Mon='TOAN'
        if self.ma[0]=='B':
            self.Mon='LY'
        if self.ma[0]=='C':
            self.Mon='HOA'
    def __str__(self):
        if self.id <10:
            if self.diem >= 18.0:
                return "GV0{} {} {} {} TRUNG TUYEN".format(self.id, self.ten,self.Mon, self.diem)
            else:
                return "GV0{} {} {} {} LOAI".format(self.id, self.ten,self.Mon, self.diem)
        else:
            if self.diem >= 18.0:
                return "GV{} {} {} {} TRUNG TUYEN".format(self.id, self.ten,self.Mon, self.diem)
            else:
                return "GV{} {} {} {} LOAI".format(self.id, self.ten,self.Mon, self.diem)
data = []
t = int(input())
for i in range(t):
    gv = GiaoVien(i+1,input(),input(),float(input()),float(input()))
    gv.tinhDiem()
    gv.xetMon()
    data.append(gv)
data = sorted(data, key= lambda x:x.diem,reverse=True)
for i in data:
    print(i)