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
    val = int(input())
    count = 0
    i = 1
    while i < val:
        if gcd(i, val) == 1:
            count +=1
        i +=1;

    if snt(count) == True:
        print("YES")
    else:
        print("NO")
    t -=1