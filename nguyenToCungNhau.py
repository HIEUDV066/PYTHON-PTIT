def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b
n, k = map(int, input().split())
t = pow(10,k-1)
count = 0
while t< pow(10,k):
    if(gcd(n,t)==1):
        print(t, end=' ')
        count +=1
    if(count == 10):
        print()
        count = 0
    t += 1