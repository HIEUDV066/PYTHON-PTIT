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
    tong = 0
    for i in s:    
        tong += int(i)
    if snt(tong) == True:
        print("YES")
    else:
        print("NO")
    t -= 1