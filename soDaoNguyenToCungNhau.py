def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b
def daoSo(n):
    s = str(n)
    n1 = s[::-1]
    return int(n1)
t = int(input())
while t != 0:
    n = int(input())
    m = daoSo(n)
    if(gcd(n,m)==1):
        print("YES")
    else:
        print("NO")
    t -=1