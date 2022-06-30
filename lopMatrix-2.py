import math

class Matrix:
    def __init__(self,n,m,a):
        self.n = n
        self.m = m
        self.a = a
    def tich(self):
        for i in range(self.n):
            for j in range(self.n):
                t = 0
                for k in range(self.m):
                    t += (self.a[i][k] * self.a[j][k])
                print(t, end=" ")
            print()
for i in range(int(input())):
    n, m = map(int, input().split())
    a=[]
    for i in range(n):
        a.append([int(j)for j in input().split()])
    matran = Matrix(n, m, a)
    matran.tich()
