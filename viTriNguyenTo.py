def snt(n):
    if n<2:
        return False
    i=2
    while i <= n/2:
        if(n%i == 0):
            return False
        i+=1
    return True
def check(s):
    for i in range(len(s)):
        if snt(i)==True and snt(int(s[i]))==False:
            return False
        if snt(i)==False and snt(int(s[i]))==True:
            return False
    return True
t = int(input())
while t != 0:
    s = input()
    if check(s)==True:
        print("YES")
    else:
        print("NO")
    t -= 1