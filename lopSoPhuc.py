class SoPhuc:
    def __init__(self,phanthuc,phanao):
        self.phanao = phanao
        self.phanthuc = phanthuc
    def __str__(self):
        a = abs(self.phanthuc)
        b = abs(self.phanao)
        if(self.phanao>0):
            return "{} + {}i".format(self.phanthuc, self.phanao)
        else:
            return "{} - {}i".format(self.phanthuc, self.phanao)
def cong(sp1:SoPhuc, sp2:SoPhuc):
    a = sp1.phanthuc + sp2.phanthuc
    b = sp1.phanao + sp2.phanao
    return SoPhuc(a,b)
def nhan(sp1:SoPhuc, sp2:SoPhuc):
    a = sp1.phanthuc*sp2.phanthuc - sp1.phanao*sp2.phanao
    b = sp1.phanthuc*sp2.phanao + sp1.phanao*sp2.phanthuc
    return SoPhuc(a,b)

t = int(input())
for i in range(t):
    a=[int(i) for i in input().split()]
    sp1 = SoPhuc(a[0], a[1])
    sp2 = SoPhuc(a[2], a[3])
    sp3 = cong(sp1, sp2)
    sp4 = nhan(sp3, sp1)
    sp5 = nhan(sp3, sp3)
    print(sp4,", ",sp5,sep="")