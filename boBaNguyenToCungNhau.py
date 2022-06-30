import math
def boBa(a, b, c):
    if (a < b < c)==False:
        return False
    if math.gcd(a,b)!=1 or math.gcd(b,c)!=1 or math.gcd(a,c)!=1:
        return False
    return True
a, b = map(int, input().split())
for i in range(a,b-1):
    for j in range(i,b):
        for k in range(j,b+1):
            if(boBa(i,j,k)==True):
                print("(" + str(i) + ", " + str(j) + ", " + str(k) +")")