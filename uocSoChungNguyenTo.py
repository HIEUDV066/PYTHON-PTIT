def snt(n):
    if n<2:
        return False
    i=2
    while i <= n/2:
        if(n%i == 0):
            return False
        i+=1
    return True
def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b
t = int(input())
while t != 0:
    so1, so2 = map(int, input().split())
    uc = gcd(so1,so2)
    sum = 0
    while uc!=0:
        sum =sum + (uc%10)
        uc = uc//10
    if snt(sum) == True:
        print("YES")
    else:
        print("NO")
    t -=1