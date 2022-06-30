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
while t!=0:
    s = input()
    count = 0
    tong = 0
    for i in range(len(s)):
        if i%2==0:
            if int(s[i])%2==1:
                count += 1
        else:
            if int(s[i])%2==0:
                count += 1
        tong += int(s[i])
    if count==0 and snt(tong)==True:
        print("YES")
    else:
        print("NO")
    t -= 1