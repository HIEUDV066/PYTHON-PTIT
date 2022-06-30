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
    count = 0
    if snt(len(s))==False:
        print("NO")
    else:
        for i in range(len(s)):
            if snt(int(s[i]))==True:
                count += 1
        if count > (len(s)-count):
            print("YES")
        else:
            print("NO")
    t -= 1