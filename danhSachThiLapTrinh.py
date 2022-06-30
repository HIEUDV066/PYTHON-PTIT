class Team:
    def __init__(self,id,sname,lname):
        self.id = str(f"Team%02d" % id)
        self.sname = sname
        self.lname = lname
    def __str__(self) -> str:
        return f"{self.sname} {self.lname}"
class ThiSinh:
    def __init__(self,id,name,team):
        self.id = str("C%03d" % id)
        self.name = name
        self.team = team
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.team}"
def mySort(A):
    return A.name
T = int(input()) + 1
A,B = dict(),list()
for i in range(1,T):
    tmp = Team(i,input(),input())
    A[tmp.id] = tmp
T = int(input()) + 1
for i in range(1,T):
    B.append(ThiSinh(i,input(),A.get(input())))
B.sort(key = mySort)
for i in B:
    print(i)


