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
    for i in s:
        if snt(int(i))==True:
            count +=1
    if snt(len(s)) == True and count > (len(s)-count):
        print("YES")
    else:
        print("NO")
    t -= 1