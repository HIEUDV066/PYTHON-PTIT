class TienDien:
    def __init__(self,i,ten,loai,cscu,csmoi):
        self.ma = "KH%02d"%(i)
        self.ten = ten
        self.loai = loai
        self.cscu = cscu
        self.csmoi = csmoi
    def chuanhoa(self):
        s = self.ten.split()
        for i in range(len(s)):
            s[i] = s[i].title()
        return " ".join(s)
    def chiso(self):
        return self.csmoi-self.cscu
    def dinhmuc(self):
        if self.loai=='A':
            return 100
        elif self.loai=='B':
            return 500
        else:
            return 200
    def trongdinhmuc(self):
        if self.chiso()<self.dinhmuc():
            return 450*self.chiso()
        else:
            return self.dinhmuc()*450
    def vuotdinhmuc(self):
        if self.chiso()>self.dinhmuc():
            return 1000*(self.chiso()-self.dinhmuc())
        else:
            return 0
    def VAT(self):
        return int(self.vuotdinhmuc()//20)
    def tongtien(self):
        return self.trongdinhmuc()+self.vuotdinhmuc()+self.VAT()
    def __repr__(self):
        return self.ma+" "+self.chuanhoa()+" "+str(self.trongdinhmuc())+" "+str(self.vuotdinhmuc())+" "+str(self.VAT())+" "+str(self.tongtien())
if __name__=='__main__':
    n = int(input())
    td = []
    for i in range(1,n+1):
        ten = input()
        loai,cscu,csmoi = input().split()
        tmp = TienDien(i,ten,loai,int(cscu),int(csmoi))
        td.append(tmp)
    td.sort(key=lambda x:x.tongtien(),reverse=True)
    for i in td:
        print(i)