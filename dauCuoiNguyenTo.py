def snt(n):
    if n<2:
        return False
    i=2
    while i <= n/2:
        if(n%i == 0):
            return False
        i+=1
    return True
t = int(input())
while t != 0:
    s = input()
    r = int(s[-3:None])
    r2 = int(s[0:3])
    if(snt(r)==True and snt(r2)==True):
        print("YES")
    else:
        print("NO")
    t -= 1