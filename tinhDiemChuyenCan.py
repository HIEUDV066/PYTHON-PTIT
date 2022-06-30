class SinhVien:
    def __init__(self, msv, ten, lop):
        self.msv = msv
        self.ten = ten
        self.lop = lop
    def __str__(self):
        return "{} {} {}".format(self.msv, self.ten, self.lop)
def tinhDiem(s):
    diem = 10
    for i in s:
        if i=='v':
            diem = diem-2
        if i=='m':
            diem = diem-1
    return diem
data = []
t = int(input())
for i in range(t):
    sv = SinhVien(input(), input(), input())
    data.append(sv)
dic = dict()
for i in range(t):
    a = [j for j in input().split()]
    d = tinhDiem(a[1])
    dic.update({a[0]:d})
for i in data:
    for j in dic:
        if j==i.msv:
            if dic[j]>0:
                print(i,dic[j],sep=" ")
            else:
                print(i,0,"KDDK",sep=" ")


